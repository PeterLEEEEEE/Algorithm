N, M = map(int, input().split())
cards = list(map(int, input().split()))

black = 0

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            if (cards[i] + cards[j] + cards[k]) <= M:
                black = max(black, cards[i] + cards[j] + cards[k])

print(black)