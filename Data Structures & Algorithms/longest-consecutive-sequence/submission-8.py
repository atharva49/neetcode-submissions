class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        maxlen = 0
        for num in nums:
            l=1
            while num+l in nums:
                l+=1

            maxlen = max(maxlen,l)

        return maxlen