class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l+=1
                
        if min_len == float("inf"):
            return 0
        return min_len
        