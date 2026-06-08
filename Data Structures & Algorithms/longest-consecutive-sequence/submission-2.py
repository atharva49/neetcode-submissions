class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        res = 0

        for n in numset:
            maximum = 1
            while n+maximum in numset:
                maximum += 1

            res =  max(res,maximum)

        return res