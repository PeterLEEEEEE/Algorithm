'''

셀프 넘버: 생성자가 없는 수
1. 1 ~ 10000까지의 숫자를 함수에 생성자를 넣어서 나오는 값은 셀프 넘버가 될 수 없음
2. 리턴되는 값을 모두 리스트에서 제거
3. 제거된 리스트에는 셀프 넘버만 남게 된다.

'''

n = 10000
arr = list(range(1,n+1))

def d(num):
    zero_3 = num // 1000
    zero_2 = (num % 1000) // 100
    zero_1 = ((num % 1000) % 100) // 10
    zero = num % 10

    return num + zero_3 + zero_2 + zero_1 + zero
for num in range(1, n+1):
    ss = d(num)
    if ss in arr:
        arr.remove(ss)

for num in arr:
    print(num)
