class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

        for i,a in enumerate(nums):
            diff = target -a

            if a in res:
                return [res.get(a),i]

            res[diff]=i

            