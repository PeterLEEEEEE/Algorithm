import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0

for i in range(len(arr)):
  ans = max(ans, i + arr[i])


print(ans+2)