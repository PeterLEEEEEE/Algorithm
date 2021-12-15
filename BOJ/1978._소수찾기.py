def is_prime(arr, ans):
    for i in arr:
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans += 1

    return ans

N = int(input())
arr = list(map(int, input().split()))
ans = 0

print(is_prime(arr, ans))