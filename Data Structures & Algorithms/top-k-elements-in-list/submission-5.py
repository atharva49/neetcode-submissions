class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        prev = {}
        for n in nums:
            prev[n] = prev.get(n,0)+1

        numLst = []
        for i,v in prev.items():
            numLst.append([v,i])
        numLst.sort()

        res = []
        while len(res)<k:
            res.append(numLst.pop()[1])

        return res




