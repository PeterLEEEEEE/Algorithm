from itertools import permutations

def solution(expression):
    answer = []
    ops = ["*","-","+"]
    for op_list in list(permutations(ops, 3)):
        print(op_list)
        op_1 = op_list[0]
        op_2 = op_list[1]
        temp_list = []
        
        for i in expression.split(op_1):
            temp = [f"({j})" for j in i.split(op_2)]
            temp_list.append(f"({op_2.join(temp)})")
        answer.append(abs(eval(op_1.join(temp_list))))
        
    return max(answer)