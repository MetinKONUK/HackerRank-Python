def hourglassSum(arr):
    n, result = len(arr), float("-inf")# Corresponds to -Infinity
    for j in range(n-2):
        for i in range(n-2):
            depth = 0
            depth += arr[j][i] + arr[j][i+1] + arr[j][i+2] # top line
            depth += arr[j+1][i+1] # middle one
            depth += arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]# bottom line
            if depth > result : result = depth # find the greatest
    return result # return the greatest
