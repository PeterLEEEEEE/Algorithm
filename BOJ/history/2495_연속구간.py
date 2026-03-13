for _ in range(3):
    arr = input()
    cnt = 1
    temp = 1
    
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            cnt += 1
            if temp < cnt:
                temp = cnt
        else:
            cnt = 1
    print(temp)
