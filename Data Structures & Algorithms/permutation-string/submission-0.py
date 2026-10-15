class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        count1 = {}
        for st in s1:
            count1[st] = 1 + count1.get(st,0)
        l=0
        count2 = {}
        for r in range(len(s2)):
            count2[s2[r]] = 1+ count2.get(s2[r],0)
            if r-l+1==len(s1):
                if count1==count2:
                    return True
                count2[s2[l]]-=1
                if count2[s2[l]]==0:
                    del count2[s2[l]]
                l+=1
        return False

