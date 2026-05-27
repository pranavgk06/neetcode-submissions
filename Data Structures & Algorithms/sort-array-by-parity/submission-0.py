class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new_arr = []
        new_odds = []
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                new_arr.append(nums[i])
                j+=1
            else:
                new_odds.append(nums[i])
        new_arr.extend(new_odds)
        return new_arr
        