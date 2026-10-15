class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
           nums1, nums2 = nums2, nums1
        #nums1 is always smallest
        m = len(nums1)
        n = len(nums2)
        total_left = (m+n+1)//2
        left = 0
        right = m
        while left<=right:
            partition1 = (left+right)//2
            partition2 = total_left - partition1
            left1Max = float("-inf") if partition1==0 else nums1[partition1-1]
            right1Min = float("inf") if partition1==m else nums1[partition1]

            left2Max = float("-inf") if partition2==0 else nums2[partition2-1]
            right2Min = float("inf") if partition2==n else nums2[partition2]

            if left1Max <= right2Min and left2Max<=right1Min:
                if (m+n)%2==0:
                    return (min(right1Min, right2Min)+max(left1Max, left2Max))/2.0
                else:
                    return max(left1Max, left2Max)
            elif left1Max>right2Min:
                right = partition1-1
            else:
                left = partition1+1
        return 0.0


