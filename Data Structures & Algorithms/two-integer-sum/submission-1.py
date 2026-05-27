class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        result = 0
        for i,n in enumerate(nums):
            result = target - nums[i]
            if result in nums_map.keys():
                return [nums_map[result], i]
            nums_map[n] = i
        