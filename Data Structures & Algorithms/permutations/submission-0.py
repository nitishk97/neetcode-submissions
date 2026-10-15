class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)
        def backtracking(curr_perm):
            if len(curr_perm) == len(nums):
                res.append(curr_perm.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                # choose one slot
                visited[i] = True
                curr_perm.append(nums[i]) #add to permutaion
                backtracking(curr_perm)

                #Backtrack
                visited[i] = False
                curr_perm.pop()
        backtracking([])
        return res




            
        