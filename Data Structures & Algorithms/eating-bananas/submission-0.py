import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 #smallest rate of bananas eaten per hour possible
        hi = max(piles) #fastest rate of bananas eaten possible

        while lo < hi:
            mid = (lo + hi) // 2

            if self.check(piles, h, mid):
                hi = mid  #if True, go lower to find more min rate
            else:
                lo = mid + 1
        return lo

    
    def check(self, piles, h, mid):
        sum_val = 0
        for i in piles:
            sum_val += math.ceil(i/mid)
        if sum_val <= h:
            return True
        return False
            