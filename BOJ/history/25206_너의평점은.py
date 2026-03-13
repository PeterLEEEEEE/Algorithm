import sys

input = sys.stdin.readline

score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0}
total_score = 0
total_credits = 0
for _ in range(20):
  name, credit, score = input().split()
  if score == 'P':
    continue
  elif score == 'F':
    total_credits += float(credit)
  else:
    total_credits += float(credit)
    total_score += (float(credit) * score_dict[score])

if total_credits == 0:
  print(format(0.0, ".6f"))
else:
  print(round(total_score / total_credits, 6))