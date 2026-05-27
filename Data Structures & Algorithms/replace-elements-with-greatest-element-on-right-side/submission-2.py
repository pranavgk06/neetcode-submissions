class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        rightMax = -1
        for i in range(len(arr) -1,-1,-1):
            newMax = max(rightMax, arr[i])
            ans[i] = rightMax
            rightMax = newMax
        return ans
            
        