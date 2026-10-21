class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            prev_max = curr_max
            prev_min = curr_min

            curr_max = max(nums[i], prev_max*nums[i], prev_min*nums[i])
            curr_min = min(nums[i], prev_max*nums[i], prev_min*nums[i])
            
            result = max(result, curr_max)
        return result