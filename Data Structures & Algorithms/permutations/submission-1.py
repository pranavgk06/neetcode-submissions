class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        result = []
        path = []

        def backtrack(i):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                path.append(nums[i])
                used.add(i)
                backtrack(used)
                path.pop()
                used.remove(i)
        
        backtrack(set())
        return result
        