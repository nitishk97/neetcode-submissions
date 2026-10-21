class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#"+"#".join(s)+"#"
        n = len(t)        
        p = [0]*n # radius at each index
        c = 0 # Center of palindrom
        r = 0 # right most edge possible
        for i in range(1,n-1):
            mirror = 2*c-i
            if i<r:
                p[i] = min(r-i, p[mirror])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i+p[i]+1]==t[i-p[i]-1]:
                p[i]+=1
            if i+p[i]>r:
                r = i+p[i]
                c=i
        maxLen = max(p)
        centerIdx = p.index(maxLen)
        start = (centerIdx-maxLen)//2
        return s[start:start+maxLen]
            

