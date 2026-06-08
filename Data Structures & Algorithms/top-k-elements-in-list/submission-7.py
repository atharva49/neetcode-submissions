class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        prev = {}

        for num in nums:
            prev[num] = prev.get(num,0)+1

        res = []
        for i,a in prev.items():
            res.append([a,i])
        
        res.sort()

        sol = []

        while len(sol)<k:
            sol.append(res.pop()[1])

        return sol