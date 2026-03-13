n, k = map(int, input().split())


def LanCnt(length):
    cnt = 0
    for i in lan:
        cnt += (i // length)

    return cnt


lan = []

for _ in range(n):
    lan.append(int(input()))

maxlan = max(lan)

start = 1
end = maxlan
tmp = 0

while start <= end:
    mid = (start + end) // 2
    if LanCnt(mid) >= k:
        tmp = mid
        start = mid + 1
    else:
        end = mid - 1

print(tmp)
