def solution(msg):
    answer = []
    msg_list = list(msg) + ["0"]
    alphabet_dict = {chr(i+64):i for i in range(1, 27)}
    num = 26
    start, end = 0, 1

    while end < len(msg_list):
        while ''.join(msg_list[start:end]) in alphabet_dict:
            end += 1
        num += 1
        alphabet_dict[''.join(msg_list[start:end])] = num

        answer.append(alphabet_dict[msg[start:end-1]])

        start, end = end - 1, end

    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))