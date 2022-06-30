from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(lambda: 0)
        
        for num in nums:
            dic[num] += 1
        
        for k, v in dic.items():
            if v > len(nums) // 2:
                return k