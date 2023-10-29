import sys

input = sys.stdin.readline

X = input().rstrip()


ans = ''
count = 0
while True:

  num = 0
  if len(X) == 1:
    break
  for char in X:
    temp = int(char)
    num += temp
  count += 1
  X = str(num)


print(count)
if (int(X) % 3 == 0):
  print("YES")
else:
  print("NO")