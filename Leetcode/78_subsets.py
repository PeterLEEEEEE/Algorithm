'''
arr = nums 리스트에 대한 checker 리스트(0, 1)
ans = 부분집합 리스트

'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr_len = len(nums)
        ans = []
        arr = [0] * arr_len

        def DFS(node):
            if node == len(nums):
                tmp = []
                for i in range(arr_len):
                    if arr[i] == 1:
                        tmp.append(nums[i])

                ans.append(tmp)

            else:
                arr[node] = 1
                DFS(node + 1)
                arr[node] = 0
                DFS(node + 1)

        DFS(0)

        return ans
