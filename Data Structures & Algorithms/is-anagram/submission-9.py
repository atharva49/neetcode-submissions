class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        prevt = {}
        prevs = {}

        for i in range(len(s)):
            prevs[s[i]] = prevs.get(s[i],0)+1
            prevt[t[i]] = prevt.get(t[i],0)+1

        return prevs==prevt