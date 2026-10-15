class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped between the bars
        # each index -> height of a bar
        # water trapped on a bar == min(hightest(bars on the left), hightest(bars on the right))

        prefix = [0]*len(height)
        suffix = [0]*len(height)
        res = 0
        for i in range(1, len(height)):
            prefix[i] = max(height[i-1], prefix[i-1])
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(height[i+1], suffix[i+1])
        for i in range(len(height)):
            res += max(0, min(suffix[i], prefix[i]) - height[i])
        return res