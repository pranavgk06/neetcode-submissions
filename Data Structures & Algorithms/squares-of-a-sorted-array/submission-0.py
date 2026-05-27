class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr2 = []
        for num in nums:
            num = pow(num,2)
            arr2.append(num)
        arr2.sort()
        return arr2

        
        