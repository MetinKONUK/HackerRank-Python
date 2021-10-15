def dynamicArray(n, queries):
    last_answer, arr, answers = 0, [[] for _ in range(n)], [] #initialize required structures
    for query in queries:
        x, y = int(query[1]), int(query[2]) #define x, y value once and for all
        if query[0] == 1: #Run this indented block if Query Type is 1
            idx = ((x ^ last_answer) % n)
            arr[idx].append(y)
        else: #Run this indented block if Query Type is 2 "There are two types of Query Types so if it's not 1 then it must be 2"
            idx = ((x ^ last_answer) % n)
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)
    return answers #Return collected answers in Query Type 2s
