class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #highest(area between 2 bars) = container with most water
        #brute force -> use 2 for loops O(n^2)
        #Optimal Approach

        l,r = 0,len(heights)-1
        res = 0
        while l<r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(area, res)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res

