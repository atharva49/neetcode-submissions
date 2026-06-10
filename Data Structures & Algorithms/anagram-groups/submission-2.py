class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        prev = defaultdict(list)

        for s in strs:
            sortString = ''.join(sorted(s))
            prev[sortString].append(s)


        return list(prev.values())

        