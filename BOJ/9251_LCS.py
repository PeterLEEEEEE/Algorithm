arr = input()
arr2 = input()

ans = 0
LCS = [[0]*(len(arr)+1) for _ in range(len(arr2)+1)]

for i in range(1, len(arr)+1):
    for j in range(1, len(arr2)+1):
        if arr[i-1] == arr2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1   
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        ans = max(ans, LCS[i][j])

print(ans)
