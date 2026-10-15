class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numToLetter = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        def dfs(i, ans):
            if i==len(digits):
                res.append("".join(ans))
                return
            current_letters = numToLetter[digits[i]]
            for letter in current_letters:
                ans.append(letter)
                dfs(i+1, ans)
                ans.pop()
        dfs(0,[])
        return res
