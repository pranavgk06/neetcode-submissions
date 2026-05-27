import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 # min possible rate to eat bananas 
        hi = max(piles)

        while lo < hi: #return val outside array
            mid = (lo + hi ) // 2

            if self.check(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1

        return hi

    def check(self, piles, h, mid):
        sum_val = 0
        for i in piles:
            sum_val += math.ceil(i/mid)
        if sum_val <= h:
            return True
        return False
            