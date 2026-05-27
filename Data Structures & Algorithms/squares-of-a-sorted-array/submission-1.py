class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr2 = []
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if (nums[l] * nums[l]) < (nums[r] * nums[r]):
                arr2.append(nums[r] * nums[r])
                r-=1
            else:
                arr2.append(nums[l] * nums[l])
                l+=1
        return arr2[::-1]

            

        
        