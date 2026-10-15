class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(subset, idx):
            if idx>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            backtrack(subset, idx+1)
            subset.pop()
            nxt_idx = idx+1
            while nxt_idx<len(nums) and nums[nxt_idx]==nums[idx]:
                nxt_idx+=1
            backtrack(subset, nxt_idx)
        backtrack([],0)
        return res
