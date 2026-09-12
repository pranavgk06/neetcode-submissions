import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if self.check(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1
        return lo

    

    def check(self, piles, mid, h):
        total_sum = 0
        for i in piles:
            total_sum += math.ceil(i/mid)
        if total_sum <= h:
            return True
        return False
        