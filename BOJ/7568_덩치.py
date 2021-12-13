N = int(input())
profile = []
for i in range(N):
    profile.append(list(map(int, input().split())))

rank = []
for flag in profile:
    cnt = 1
    for j in profile:
        if flag[0] < j[0] and flag[1] < j[1]:
            cnt += 1
    
    rank.append(cnt)

print(*rank, sep=' ')

