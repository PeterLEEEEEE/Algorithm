n, m = map(int, input().split())

arr = []


for _ in range(n+m):
    arr.append(input())

part1 = arr[:n]
part2 = arr[n:]

set1 = set(part1)
set2 = set(part2)
ans = list(set1 & set2)
ans.sort()

print(len(ans))

for i in ans:
    print(i)

