class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0

        for num in numset:
            l = 1
            while num+l in numset:
                l+=1

            maxlen = max(maxlen,l)


        return maxlen