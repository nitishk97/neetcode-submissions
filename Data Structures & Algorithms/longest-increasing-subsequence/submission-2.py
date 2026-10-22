from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            if idx==len(sub):
                sub.append(num)
            sub[idx]=num
        return len(sub)

            