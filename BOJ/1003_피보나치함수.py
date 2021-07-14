n = int(input())

cnt0 = [1, 0]
cnt1 = [0, 1]

for _ in range(n):
    num = int(input())

    if num == 0:
        print(cnt0[0], cnt0[1])
    elif num == 1:
        print(cnt1[0], cnt1[1])

    else:
        for i in range(2, num + 1):
            cnt0.append(cnt0[i-1] + cnt0[i-2])
            cnt1.append(cnt1[i-1] + cnt1[i-2])

        print(f'{cnt0.pop()} {cnt1.pop()}')

        cnt0 = [1, 0]
        cnt1 = [0, 1]

# 재귀로 풀면 시간초과
# n = int(input())

# def fibo(n):
#     if n == 0:
#         arr[0] += 1
#         return 0
#     elif n == 1:
#         arr[1] += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# for _ in range(n):
#     num = int(input())
#     arr = [0, 0]
#     fibo(num)
#     print(arr[0], arr[1])
