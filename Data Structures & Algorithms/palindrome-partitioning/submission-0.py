class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = []
        def isPalindrome(st):
            return st == st[::-1]
        # start -> cut the slice of the loaf
        def dfs(start, ans):
            if start==len(s):
                res.append(ans.copy())
            
            for end in range(start+1, len(s)+1):
                substring = s[start:end]
                if isPalindrome(substring):
                    ans.append(substring)
                    dfs(end, ans)
                    ans.pop()
        dfs(0,[])
        return res


                    




            

        