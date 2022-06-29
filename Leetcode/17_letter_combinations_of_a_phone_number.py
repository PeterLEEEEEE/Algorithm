from itertools import combinations
dic = {'2':'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
print(dic)

digits = '23'

ans = []
for i in range(len(digits)):
    temp = list(dic[digits[i]])

    for j in combinations(temp, 2):
        