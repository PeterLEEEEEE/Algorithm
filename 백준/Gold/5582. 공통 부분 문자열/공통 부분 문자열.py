# LCS Algorithm

import sys
from collections import deque

input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
col = len(word2)+1
row = len(word1)+1
dp = [[0] * col for _ in range(row)]

ans = 0
for i in range(1, row):
  for j in range(1, col):
    if word1[i-1] == word2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1

ans = max(map(max, dp))

if ans == 1:
  print(0)
else:
  print(ans)




