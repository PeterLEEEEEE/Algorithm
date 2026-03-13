num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

ans = num1 + num2

ans = str(ans)
ans = ans[::-1]

print(int(ans))