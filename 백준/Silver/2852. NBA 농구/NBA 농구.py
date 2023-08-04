import sys

def str_to_second(score_time):
  minutes, seconds = score_time.split(':')

  return (int(minutes) * 60) + int(seconds)


input = sys.stdin.readline

N = int(input())

MAX_TIME = 60 * 48
score_dict = {'1': 0, '2': 0}
score_time_dict = {'1': 0, '2': 0}
ans = {'1': 0, '2': 0}

cur_winning_team = '0'

for _ in range(N):
  team, score_time = input().split()

  score_time = str_to_second(score_time)

  score_dict[team] += 1

  if cur_winning_team == '0':
    cur_winning_team = team
    score_time_dict[team] = score_time
  elif cur_winning_team != '0' and score_dict['1'] == score_dict['2']:
    ans[cur_winning_team] += score_time - score_time_dict[cur_winning_team]
    cur_winning_team = '0'

if cur_winning_team != '0':
  ans[cur_winning_team] += MAX_TIME - score_time_dict[cur_winning_team]

team1_min = ans['1'] // 60
team1_sec = ans['1'] % 60
team2_min = ans['2'] // 60
team2_sec = ans['2'] % 60
print(f"{team1_min:02}:{team1_sec:02}")
print(f"{team2_min:02}:{team2_sec:02}")
