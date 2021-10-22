def connectedCell(matrix):
    rows = len(matrix) #Rows count
    columns = len(matrix[0]) #Columns count
    blobs = 0 #A 0 initialized value to comparison (It is the lowest value possible)
    def blob_detection(r, c): # Defined a function for recursive "1" finding
        if (r >= rows) or (c >= columns) or (r < 0) or (c < 0): return 0 #A escape case for invalid addresses
        if matrix[r][c] == 0: return 0 #If the location keeps a "0" then no need to search anymore
        #If the programme run till this line then it means we found a "1"
        matrix[r][c] = 0  #Turn "1" into a "0"to avoid infinite recursion
        return 1+blob_detection(r-1, c-1)+blob_detection(r-1, c)+blob_detection(r-1, c+1)+blob_detection(r, c-1)+blob_detection(r, c+1)+blob_detection(r+1, c-1)+blob_detection(r+1, c)+blob_detection(r+1, c+1)
        #Scanning all adjacents of 1 in the above line in recursion
    for r in range(rows): #Searching through the matrix to find "1"s
        for c in range(columns):
            result = blob_detection(r, c)
            if result > blobs: #If result of the recursion is greater than the previous result then current result is our candidate for final result
                blobs = result
    return blobs #return the final-maximum blob count as the solution of the problem
