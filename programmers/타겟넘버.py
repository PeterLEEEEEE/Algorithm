ans = 0

def dfs(numbers, target, score, idx):
    if idx >= len(numbers):
        if score == target:
            global ans 
            ans += 1
        return

    dfs(numbers, target, score+numbers[idx], idx+1)
    dfs(numbers, target, score-numbers[idx], idx+1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)

    return ans


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(solution(numbers, target))