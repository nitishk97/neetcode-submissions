class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = -1*heapq.heappop(stones)
            stone2 = -1*heapq.heappop(stones)
            if stone1>stone2:
                heapq.heappush(stones, stone2-stone1)
            elif stone2>stone1:
                heapq.heappush(stones, stone1-stone2)
            else:
                continue
        return -stones[0] if stones else 0
