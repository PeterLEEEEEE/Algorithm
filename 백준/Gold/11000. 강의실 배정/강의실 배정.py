import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: -x[0])

start, finish = arr.pop()
endTime = [finish]
answer = 1
while arr:
    finish = endTime[0]
    s, f = arr.pop()
    if s < finish:
      answer += 1
    else:
      heapq.heappop(endTime)
    heapq.heappush(endTime, f)

print(answer)