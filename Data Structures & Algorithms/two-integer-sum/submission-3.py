class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev = {}

        for i,a in enumerate(nums):
            diff = target - a

            if a in prev:
                return [prev[a],i]

            prev[diff] = i