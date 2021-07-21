n = int(input())

money = 1000 - n

arr = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in arr:
    if money == 0:
        break
    if money >= i:
        cnt += (money // i)
        money = money % i

print(cnt)
