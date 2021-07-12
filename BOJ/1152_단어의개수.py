
# 내 풀이
n = input()

cnt = 0
arr = list(n.split(' '))
for i in arr:
    if i != '':
        cnt += 1

print(cnt)

# 다른 풀이

n = input().split()
print(len(n))