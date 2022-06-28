def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(rows):
        temp = i * columns + 1
        arr.append([j for j in range(temp, temp+columns)])
    
    for q in queries:
        y1, x1, y2, x2 = q
        temp = arr[y1-1][x1-1]
        min_num = max(arr[rows-1])

        for i in range(y1-1, y2-1):
            arr[i][x1-1] = arr[i+1][x1-1]
            min_num = min(min_num, arr[i+1][x1-1])
        
        for i in range(x1-1, x2-1):
            arr[y2-1][i] = arr[y2-1][i+1]
            min_num = min(min_num, arr[y2-1][i+1])
        
        for i in range(y2-1, y1-1, -1):
            arr[i][x2-1] = arr[i-1][x2-1]
            min_num = min(min_num, arr[i-1][x2-1])
        
        for i in range(x2-1, x1, -1):
            arr[y1-1][i] = arr[y1-1][i-1]
            min_num = min(min_num, arr[y1-1][i-1])
        
        arr[y1-1][x1] = temp
        min_num = min(min_num, temp)
        answer.append(min_num)
    
    print(arr)
    # for q in queries:
    #     answer.append(min(queries[q[0]-1][q[1]-1 : q[-1]-q[1]]))
    return answer

rows, columns = 6, 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))
