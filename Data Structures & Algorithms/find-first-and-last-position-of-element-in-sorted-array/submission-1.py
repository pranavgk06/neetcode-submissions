class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        new_list = []
        if len(nums) == 0:
            return [-1,-1]
        if target > max(nums) or target < min(nums):
            return [-1,-1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        new_list.append(lo)

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        new_list.append(hi)
 
        if new_list[0] > new_list[1]:
            return [-1, -1]
        return new_list


        
        


        
        
        
        

        