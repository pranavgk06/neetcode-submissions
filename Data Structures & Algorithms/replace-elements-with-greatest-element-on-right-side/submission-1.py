class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        for i in range(0, len(arr)):
            new_arr.append(max(arr))
            arr.remove(arr[0])
        new_arr.append(-1)
        new_arr.remove(new_arr[0])
        return new_arr
        