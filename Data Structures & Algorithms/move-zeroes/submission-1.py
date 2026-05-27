class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
                i+=1
            else:
                i+=1

        while j <= len(nums) - 1:
            nums[j] = 0
            j+=1