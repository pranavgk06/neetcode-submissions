class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        count = 0
        for num in nums:       
            if num - 1 not in seen:
                count = 1
                while num + 1 in seen:
                    count += 1
                    num += 1
                max_len = max(max_len, count)

        return max_len

        