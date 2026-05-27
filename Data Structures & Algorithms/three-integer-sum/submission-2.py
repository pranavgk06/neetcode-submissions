class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue 

            l = i+1
            r = len(nums) - 1

            while l < r:
                val = a + nums[l] + nums[r]
                if val > 0:
                    r-=1
                elif val < 0:
                    l+=1
                else:
                    new_list.append([a,nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
        return new_list