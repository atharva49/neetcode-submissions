class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = list(set(nums))

        max_len = 0
        for num in nums:
            longest = 1
            while num+1 in nums:
                longest+=1
                num+=1

            max_len = max(max_len,longest)

        return max_len