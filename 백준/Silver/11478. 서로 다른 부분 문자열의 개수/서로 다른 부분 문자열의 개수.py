import sys
input = sys.stdin.readline

S = input().rstrip()


list_s = list(S)
# print(list_s)
ans = []
for j in range(len(S)):
  for i in range(len(S)):
    if i+j > len(S):
      break
    ans.append(S[i:i+j])

print(len(set(ans)))