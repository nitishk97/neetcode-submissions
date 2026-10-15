class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, idx, nums):
            if idx>=len(nums):
                res.append(subset.copy())
                return
            
            #include nums[i]
            subset.append(nums[idx])
            backtrack(subset, idx+1, nums) #go forward
            subset.pop() #backtrack

            backtrack(subset, idx+1, nums)
        backtrack([], 0, nums)
        return res
            
            
            