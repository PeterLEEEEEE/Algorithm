def solution(n, arr1, arr2):
    answer = []
    b_arr1 = []
    b_arr2 = []
    for i in arr1:
        temp = format(i, 'b')
        if len(temp) == (n - 1):
            temp = '0' + temp
        
        b_arr1.append(temp)
    
    for i in arr2:
        temp = format(i, 'b')
        if len(temp) < n:
            temp = '0'*(n-len(temp)) + temp
        
        b_arr2.append(temp)

    print(b_arr2)
    for i in range(n):
        temp = ''
        for j in range(n):
            
            if int(b_arr1[i][j]) + int(b_arr2[i][j]) == 0:
                temp += ' '
            else:
                temp += '#'

        answer.append(temp)
    print(answer)
    # return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(5, arr1, arr2)