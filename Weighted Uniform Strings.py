def weightedUniformStrings(s, queries):
    arr, i, start = set(), 0, 0 #The only trick of this problem is using set instead of an array.
    while True:
        if i == len(s)-1:
            x = s[start:]
            for j in range(1, len(x)+1):
                arr.add((ord(x[0])-96)*j)
            break
        elif s[i] != s[i+1]:
            x = s[start:i+1]
            for j in range(1, len(x)+1):
                arr.add((ord(x[0])-96)*j)
            start = i+1
        i+=1
    return ["Yes" if q in arr else "No" for q in queries]
  #Using set prevents adding same numbers again and again to the memory and buys us space and much more importantly: Time.
