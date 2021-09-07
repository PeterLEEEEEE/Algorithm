arr = []
ans = []
for _ in range(5):
    arr.append(input())

for i in range(5):
    if 'FBI' in arr[i]:
        ans.append(i+1)
        
if not ans:
    print("HE GOT AWAY!")
for i in ans:
    print(i, end=' ')
