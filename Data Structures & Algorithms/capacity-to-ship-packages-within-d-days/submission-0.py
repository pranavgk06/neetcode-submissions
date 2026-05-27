import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            
            if self.check(weights, days, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


    def check(self, weights, days, mid):
        days_needed = 1 #number of days, number of ship export trips
        current_weight = 0

        for i in weights:
            if current_weight + i > mid: #capacity too high, so we ship
                days_needed +=1 #add a ship trip
                current_weight = 0 #reset 
            current_weight+=i #add after if to not go over ceiling
        return days_needed <= days

        

        