class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        asc = []
        for i,a in count.items():
            asc.append([a,i])

        asc.sort()
        res = []

        while len(res) < k:
            res.append(asc.pop()[1])

        return res