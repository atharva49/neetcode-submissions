class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        prev = defaultdict(list)

        for s in strs:
            sorteds = ''.join(sorted(s))
            prev[sorteds].append(s)


        return list(prev.values())