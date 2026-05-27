class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
            else:
                return True
        return False
        