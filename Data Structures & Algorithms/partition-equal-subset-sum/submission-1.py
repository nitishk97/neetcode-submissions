class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        target=0
        for num in nums:
            total+=num
        if total%2!=0:
            return False
        target = total // 2
        def dfs(idx, curr):
            if curr==target:
                return True
            if idx==len(nums) or curr>target:
                return False
            return dfs(idx+1, curr+nums[idx]) or dfs(idx+1, curr)
        return dfs(0,0)

