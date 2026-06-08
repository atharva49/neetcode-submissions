class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev = {}
        for k,v in enumerate(nums):
            diff = target-v

            if v in prev:
                return [prev.get(v),k]

            prev[diff] = k