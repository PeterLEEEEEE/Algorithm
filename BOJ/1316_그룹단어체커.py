'''
개고생해서 푼 문제...

'''

n = int(input())

arr = []
cnt = 0

for _ in range(n):
    words = input()
    arr.append(words)


def checker(tmp, cnt):

    for i in range(len(tmp) - 1):
        if tmp[i] != tmp[i+1]:
            if tmp[i] in tmp[i+1:]:
                break

    else:
        cnt += 1

    return cnt


for tmp in arr:
    cnt = checker(tmp, cnt)

print(cnt)
