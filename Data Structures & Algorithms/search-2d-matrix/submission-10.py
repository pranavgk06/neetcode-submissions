class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = col * row - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
                

        

                

        