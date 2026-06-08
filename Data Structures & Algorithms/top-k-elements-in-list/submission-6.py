class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        prev = {}

        for num in nums:
            prev[num] = prev.get(num,0)+1


        ordered = []
        for i,v in prev.items():
            ordered.append([v,i])

        ordered.sort()

        res = []

        while len(res) < k:
            res.append(ordered.pop()[1])

        return res