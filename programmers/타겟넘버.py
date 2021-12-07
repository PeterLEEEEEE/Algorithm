def dfs(numbers, target, score, idx, ans):
    if idx == len(numbers):
        pass
    return ans

def solution(numbers, target):
    ans = dfs(numbers, target, 0, 0, 0)

    return ans


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(solution(numbers, target))