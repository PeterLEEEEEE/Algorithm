n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

tmp = []
team = []

for i in range(n):
    tmp.append(arr[i][0])



for i in tmp:
    if tmp.count(i) >= 5:
        if i not in team:
            team.append(i)



if team:
    print(''.join(sorted(team)))
else:
    print('PREDAJA')