class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        length = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len


        