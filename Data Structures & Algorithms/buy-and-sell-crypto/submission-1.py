class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        
        for p in prices:
            best = max(best, p - min_price)
            min_price = min(min_price,p)
        return best
        