from collections import defaultdict

def solution(weights):
  answer = 0
  weight_dict = defaultdict(int)
  print(weight_dict)
  for weight in weights:
    answer += weight_dict[weight] + weight_dict[weight*2] + \
              weight_dict[weight*2/3] + weight_dict[weight*3/2] + \
              weight_dict[weight*4/3] + weight_dict[weight*3/4] + weight_dict[weight/2]
    weight_dict[weight] += 1
  return answer

weights = [100, 180, 360, 100, 270]

print(solution(weights))