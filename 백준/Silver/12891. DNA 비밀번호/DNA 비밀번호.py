import sys

input = sys.stdin.readline

S, P = map(int, input().split())
DNA = list(input().rstrip())
A, C, G, T = map(int, input().split())

left, right = 0, P-1
temp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

ans = 0
for i in range(P):
  temp[DNA[i]] += 1


while right < S:

  if temp['A'] >= A and temp['C'] >= C and temp['G'] >= G and temp['T'] >= T:
    ans += 1

  if temp[DNA[left]] > 0:
    temp[DNA[left]] -= 1
  left += 1
  right += 1
  if right < S:
    temp[DNA[right]] += 1

print(ans)



