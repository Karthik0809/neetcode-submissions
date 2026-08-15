class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        res = r
        while l <= r:
            totaltime = 0
            k = l +((r-l) // 2)
            
            for p in piles:
                totaltime += math.ceil(float(p) / k)
            if totaltime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res



