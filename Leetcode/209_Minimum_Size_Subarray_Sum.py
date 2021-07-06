class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summa = 0
        start = 0
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        
        arr = []
        
        for idx in range(len(nums)):
            summa += nums[idx]
            
            while summa >= target:
                arr.append(idx + 1 - start)
                summa -= nums[start]
                start += 1
        
        
        return min(arr)