import sys


input = sys.stdin.readline


def solution(cur, target):
  ans = abs(cur - target)
  if ans <= len(str(target)):
    return ans

  for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
            # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
            if int(nums[j]) in buttons:
                break

            # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
            elif j == len(nums) - 1:
                ans = min(ans, abs(int(nums) - target) + len(nums))

  return ans

if __name__ == '__main__':
  # write input
  N = int(input())
  M = int(input())
  buttons = []
  if M:
    buttons = list(map(int, input().split()))

  if N == 100:
    print(0)
  else:
    print(solution(100, N))