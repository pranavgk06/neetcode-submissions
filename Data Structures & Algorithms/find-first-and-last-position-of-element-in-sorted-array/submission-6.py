class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = []
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if lo >= len(nums) or nums[lo] != target:
            return [-1,-1]
        arr.append(lo)

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1 
            else:
                hi = mid - 1
        arr.append(hi)
        return arr
        