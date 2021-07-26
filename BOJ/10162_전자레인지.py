import sys
time = int(sys.stdin.readline())

timer = [300, 60, 10]
cnt = [0, 0 ,0]

for i in range(len(timer)):
    if time % 10 != 0:
        print(-1)
        break
    else:
        if time >= timer[i]:
            cnt[i] = time // timer[i]
            time %= timer[i]
else:            
    for i in cnt:
        print(i, end=' ')
            
