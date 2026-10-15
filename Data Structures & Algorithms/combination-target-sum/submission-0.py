class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, count, idx, nums, target):
            if count==target:
                res.append(subset.copy())
                return
            if count>target or idx>=len(nums):
                return
            
            #include the num
            count+=nums[idx]
            subset.append(nums[idx])
            backtrack(subset, count, idx, nums, target) # re-use same index
            count-=nums[idx]
            subset.pop() # backtrack

            backtrack(subset, count, idx+1, nums, target) # exclude the num
        backtrack([], 0, 0, nums, target)
        return res

        

