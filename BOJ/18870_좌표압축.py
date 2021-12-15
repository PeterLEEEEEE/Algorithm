import sys
input = sys.stdin.readline

N = int(input())
cord = list(map(int, input().split()))

sorted_cord = sorted(set(cord))

ans = {}
for i in range(len(sorted_cord)):
    ans[sorted_cord[i]] = i

for i in cord:
    print(ans[i], end = ' ')