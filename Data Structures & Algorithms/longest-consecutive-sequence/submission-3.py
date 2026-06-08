class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = set(nums)

        max_cnt = 0

        for num in nums:
            length = 1
            while num+length in res:
                length += 1

            max_cnt = max(max_cnt,length)


        return max_cnt