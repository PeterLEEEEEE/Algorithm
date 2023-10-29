import sys

input = sys.stdin.readline

M, N = map(int, input().split())

dic = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
dic2 = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
str_list = []
numToStr = ''
for i in range(M, N+1):
  if len(str(i)) == 1:
    numToStr = dic[str(i)]
  else:
    temp1, temp2 = dic[str(i)[0]], dic[str(i)[1]]
    numToStr = f"{temp1} {temp2}"
  str_list.append(numToStr)

str_list.sort()

ans = []

for numStr in str_list:
  ll = numStr.split()
  if len(ll) == 1:
    ans.append(dic2[ll[0]])
  else:
    ans.append(dic2[ll[0]]+dic2[ll[1]])

cnt = 0
for i in ans:
  cnt += 1
  print(i, end=' ')

  if cnt == 10:
    print()
    cnt = 0