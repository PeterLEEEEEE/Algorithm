n, price = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse = True)
cnt = 0

for coin in coins:
    if coin <= price:
        cnt += (price // coin)
        price = price % coin
        
        if price == 0:
            break
print(cnt)