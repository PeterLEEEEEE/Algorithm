def solution(N, number):
    answer = 0
    s = [set() for _ in range(8)]
    
    for idx, x in enumerate(s, start=1):
        x.add(int(str(N) * idx))
    print(x)
    return answer
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[[i - j - 1]]:
                    pass
N = 5
number = 12
print(solution(N, number))