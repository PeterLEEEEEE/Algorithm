import sys

input = sys.stdin.readline


idx = 0
while True:
  word = input().rstrip()
  if "-" in word:
    break

  ans = 0
  idx += 1
  stack = []

  for w in word:
    if w == '{': # 여는 괄호인 경우
      stack.append(w)
    else: # 닫는 괄호인 경우
      if stack: # 스택에 여는 괄호가 있는 경우
        temp = stack.pop()
      else: # 스택에 여는 괄호가 없는 경우
        ans += 1
        stack.append('{')

  if len(stack) >= 2:
    ans += (len(stack) // 2)

  print(f"{idx}. {ans}")