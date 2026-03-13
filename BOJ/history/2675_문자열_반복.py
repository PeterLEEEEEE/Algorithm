'''
n = 몇 번 입력할 것인지
num = 반복될 알파벳 횟수
word = 단어
word를 루프 돌며 num 횟수만큼 반복 출력

'''

n = int(input())

for _ in range(n):
    num, word = input().split()
    for al in word:
        print((al * int(num)), end='')
    print()
