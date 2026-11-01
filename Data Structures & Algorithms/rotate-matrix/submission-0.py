class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1 2 3     7 4 1
        # 4 5 6 --> 8 5 2
        # 7 8 9     9 6 3

        # [row, col] --> [col, n - row]
        # [0, 0] --> [0, n (n - 0)]
        # [1, 0] --> [0, n - 1]
        # [n, 0] --> [0, 0 (n - n)]
        # [n, 1] --> [1, n - 1]
        # [n, n] --> [n, 0 (n - n)]
        rotated = set()
        n = len(matrix)

        for row in range(n):
            for col in range(n):
                if (row, col) in rotated:
                    continue

                prev = matrix[row][col]
                while (row, col) not in rotated:
                    temp = matrix[col][n - 1 - row]
                    matrix[col][n - 1 - row] = prev
                    rotated.add((row, col))
                    row, col = col, n - 1 - row
                    prev = temp
