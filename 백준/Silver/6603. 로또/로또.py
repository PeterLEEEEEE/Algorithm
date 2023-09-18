import sys
import copy

input = sys.stdin.readline


def solution(lev):

  if lev == 6:
    ans.add((" ".join(map(str, sorted(selected)))))


    return

  for i in range(len(nums)):
    if visited[i]:
      continue

    visited[i] = True
    selected.append(nums[i])

    solution(lev+1)

    selected.pop()
    visited[i] = False

if __name__ == '__main__':
  # write input

  while True:
    temp = list(map(int, input().split()))
    visited = [False] * temp[0]
    selected = []
    ans = set()
    if temp[0] == 0 or len(temp) == 0:
      break

    nums = copy.deepcopy(temp[1:])

    solution(0)
    ans = list(ans)
    new_ans = []
    for num in ans:
      num = list(map(int, num.split()))
      new_ans.append(num)

    new_ans.sort()

    for i in new_ans:
      print(*i)

    print()
