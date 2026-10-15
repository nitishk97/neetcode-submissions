class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # each hour you get to eat only one pile
        # return min k such that you complete all piles in h hours
        # num of hours to complete a pile = piles[i]/k
        # k = num of bananas/hour
        # lowest k = 1
        # hightest k = max(piles)
        l = 1
        r = max(piles)
        res = float("inf")
        while l<=r:
            mid = (l+r)//2
            total=0
            for pile in piles:
                total+=math.ceil(float(pile) / mid)
            if total<=h:
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        return res

