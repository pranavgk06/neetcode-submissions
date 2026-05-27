class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            low = 0
            high = len(matrix[row]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

                

        