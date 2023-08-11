import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

friends = defaultdict(int)
invite = set()

for _ in range(m):
  a, b = map(int, input().split())
  friends[a] = friends.get(a, []) + [b]
  friends[b] = friends.get(b, []) + [a]

# def bfs(a):

#   queue = deque()
#   queue.append()
if not friends[1]:
  print(0)
else:
  for friend in friends[1]:

    invite.add(friend)

    if friends[friend]:
      for f in friends[friend]:
        invite.add(f)

  print(len(invite) - 1)

