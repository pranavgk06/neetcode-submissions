class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i])
                path.pop()

        backtrack(0, target)
        return result
        