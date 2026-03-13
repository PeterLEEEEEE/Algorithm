'''
string 라이브러리를 통해 a~z까지의 알파벳을 alpha에 저장

  alpha 만큼 루프를 돌면서 n의 몇 번째 인덱스에 해당 알파벳이 존재하는 지를 체크해서 num 변수에 담고 바로 출력, 없으면 -1 출력

'''


import string
n = input()
alpha = string.ascii_lowercase

num = 0

for alphabet in alpha:
    if alphabet in n:
        num = n.index(alphabet)
    else:
        num = -1
    print(num, end= ' ')
