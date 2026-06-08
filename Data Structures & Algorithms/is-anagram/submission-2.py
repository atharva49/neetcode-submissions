class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        prevS = {}
        prevT = {}

        for i in range(len(s)):
            prevS[s[i]] = prevS.get(s[i],0)+1
            prevT[t[i]] = prevT.get(t[i],0)+1

        return prevS == prevT