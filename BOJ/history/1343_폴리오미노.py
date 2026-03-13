import re, sys
input = sys.stdin.readline

txt = input().rstrip()

result = re.findall(r'(X+|\.+)', txt)
ans = []

flag = 1

for poly in result:

  if poly.find('X') == -1:
    ans.append(poly)
  elif len(poly) % 4 == 0:
    ans.append('AAAA' * (len(poly) // 4))
  elif len(poly) % 4 == 2:
    ans.append('AAAA' * (len(poly) // 4) + 'BB')
  elif len(poly) == 2:
    ans.append('BB')

  else:
    flag = -1
    break

if flag == -1:
  print(flag)
else:
  print(''.join(ans))