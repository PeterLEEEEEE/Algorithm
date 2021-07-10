'''
몫과 나머지를 구해서 100의 자리, 10의 자리, 1의 자리 수를 추출해낼 수 있으면 쉬운 문제

ex. 
n = 123
100의 자리 수: n // 100 = 1

n % 100 = 23

10의 자리 수: (n % 100) // 10
1의 자리 수: (n % 100) % 10

'''


n = int(input())

cnt = 0
if n >= 100:
    cnt = 99

    for i in range(100, n+1):
        hundreds = i // 100
        tens = (i % 100) // 10
        ones = (i % 100) % 10
        if (hundreds - tens) == (tens - ones):
            cnt+=1
    print(cnt)

else:
    print(n)
