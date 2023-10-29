import sys
input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

start = arr[0] - 0.5
end = start + L
ans = 1

for i in range(len(arr)):
  if start < arr[i] < end:
    continue
  else:
    ans+=1
    start = arr[i] - 0.5
    end = start + L

print(ans)