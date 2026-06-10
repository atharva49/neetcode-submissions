class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        maxlen = 0

        for num in nums:
            length = 1
            while num+length in nums:
                length+=1

            maxlen = max(maxlen,length)


        return maxlen