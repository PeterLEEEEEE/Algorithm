# 기름값이 최소인 곳을 찾아서 거리와 곱함, 기름 값이 높다면 그냥 무시함, 최소-최대값 문제랑 비슷하다

city = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cost = cost[:len(cost)-1]

cheapest = 1000000001
ans = 0

for i in range(len(cost)):
    if cheapest > cost[i]:
        cheapest = cost[i]
    ans += (cheapest * distance[i])


print(ans)
