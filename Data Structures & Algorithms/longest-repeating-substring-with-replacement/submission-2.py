class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        char = {}
        res = 0
        maxf=0
        for r in range(len(s)):
            char[s[r]] = 1+ char.get(s[r],0)
            maxf = max(maxf, char[s[r]])
            while r-l+1 - maxf >k:
                char[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
        return res