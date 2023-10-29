def to_binary(ones):
  len_ones = len(ones)
  bi = format(int(len_ones), 'b')

  return bi

def solution(s):
  answer = []
  cnt = 0
  while True:
    zero_cnt = 0
    if s == "1":
      break
    list_s = list(s)
    ones = ""
    print(list_s)
    for i in list_s:
      if i == '0':
        zero_cnt += 1
      else:
        ones += "1"

    s = to_binary(ones)
    answer.append(zero_cnt)
    cnt += 1

  return [cnt, len(answer)]

s = "110010101001"

print(solution(s))