def solution(sequence, k):
    answer = []
    if sequence[-1] == k:
        return [len(sequence)-1, len(sequence)-1]

    left_idx = 0
    right_idx = -1
    cur_val = 0

    while True:
        if cur_val < k:
            right_idx += 1
            if right_idx >= len(sequence):
                break
            cur_val += sequence[right_idx]
        else:
            cur_val -= sequence[left_idx]
            if left_idx >= len(sequence):
                break
            left_idx += 1

        if cur_val == k:
            answer.append([left_idx, right_idx])

    answer.sort(key=lambda x:(x[1]-x[0], x[0]))



    return answer[0]

sequence = [2, 2, 2, 2, 2]
k = 6

print(solution(sequence, k))