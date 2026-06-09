class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        prev = {}

        for num in nums:
            prev[num] = prev.get(num,0)+1

        elem = []
        for i,a in prev.items():
            elem.append([a,i])

        elem.sort()
        res = []
        while len(res) < k:
            res.append(elem.pop()[1])

        return res