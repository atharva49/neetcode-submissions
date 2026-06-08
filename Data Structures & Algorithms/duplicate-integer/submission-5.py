class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nusm_dedup = list(set(nums))
        print(nusm_dedup)
        print(nums)
        return not len(nusm_dedup )== len(nums)