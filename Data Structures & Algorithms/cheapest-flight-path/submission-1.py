class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        # use bellman ford alrorithm -> for every flight we find the cheapest prices to each node
        prices[src]=0
        for _ in range(k+1):
            tmp_prices = prices.copy()
            for u,v,price in flights: # get's cheapest price from each node
                if prices[u]==float("inf"):
                    continue
                if price+prices[u]<tmp_prices[v]:
                    tmp_prices[v]=price+prices[u]
            prices = tmp_prices
        if prices[dst]==float("inf"):
            return -1
        return prices[dst]
