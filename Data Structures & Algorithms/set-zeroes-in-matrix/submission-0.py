class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowZero = any(number == 0 for number in matrix[0])
        firstColumnZero = any(row[0] == 0 for row in matrix)
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        def zeroRow(row):
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

        def zeroCol(col):
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                zeroRow(i)
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                zeroCol(j)
        
        if firstRowZero:
            zeroRow(0)
        if firstColumnZero:
            zeroCol(0)