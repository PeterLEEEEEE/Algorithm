complex = int(input())

complexes = []
cnt = 0
ans = [0]


def dfs(y, x):
    global cnt
    if y >= complex or x >= complex or y < 0 or x < 0:
        return False
    if complexes[y][x] == 0:
        return False

    complexes[y][x] = 0
    cnt += 1

    dfs(y+1, x)
    dfs(y, x+1)
    dfs(y-1, x)
    dfs(y, x-1)

    return True


for _ in range(complex):
    complexes.append(list(map(int, input())))

for y in range(complex):
    for x in range(complex):
        search = dfs(y, x)
        if search:
            ans[0] += 1
            ans.append(cnt)
            cnt = 0

ans = ans[:1] + sorted(ans[1:])
# print(type(ans[0]))  # int
# print(ans[0])  # int 3
# print(type(ans[:1]))  # list
# print(ans[:1])  # list [3]
print(*ans, sep='\n')
