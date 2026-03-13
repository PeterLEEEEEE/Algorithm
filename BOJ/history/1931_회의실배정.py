# greedy algorithm
'''
이중 리스트의 경우 정렬을 하게 되면 안에 있는 0번째 인덱스 값을 기준으로 정렬하게 되기 때문에
1번 째 인덱스를 우선 순위로, 차순위를 0번 째로 정렬시켜주기 위해 lambda식 사용
'''
n = int(input())
tmp = []
ans = 0
cnt = 0
flag = 0

for _ in range(n):
    s, e = map(int, input().split())
    tmp.append([s, e])

ans = sorted(tmp, key=lambda x: x[1])
print(ans)
for s, e in ans:
    if s >= flag:
        flag = e
        cnt += 1

print(cnt)
