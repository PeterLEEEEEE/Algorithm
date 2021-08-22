n = int(input())

for _ in range(n):
    arr = input().split()
    flag = int(arr[0]) - 1
    ans = list(arr[1])
    ans.pop(flag)
    

    print(''.join(ans))
    
    