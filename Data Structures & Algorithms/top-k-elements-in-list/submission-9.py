class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        prev = {}

        for num in nums:
            prev[num] = prev.get(num,0)+1

        asc = []
        for i,a in prev.items():
            asc.append([a,i])
        asc.sort()

        res = []
        while len(res) < k:
            res.append(asc.pop()[1])

        return res