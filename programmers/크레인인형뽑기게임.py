def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            target = board[j][i-1]
            if target != 0:
                if not stack:
                    stack.append(target)
                else:
                    if stack[-1] == target:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(target)
                board[j][i-1] = 0
                break
    return answer

if __name__ == '__main__':
    board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]

    moves = [1,5,3,5,1,2,1,4]

    print(solution(board, moves))