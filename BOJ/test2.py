from collections import deque
q = deque()
q.append([0, 0])
x, y = q.popleft()

print(x, y)

