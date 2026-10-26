class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low < high - 1:
            mid = low + (high - low) // 2
            num = matrix[mid][0]

            if num == target:
                return True
            elif num > target:
                high = mid -1
            else:
                low = mid
        
        row = low if target < matrix[high][0] else high

        low = 0
        high = len(matrix[row]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            num = matrix[row][mid]

            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False