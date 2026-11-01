class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        remaining = [len(matrix[0]), len(matrix) - 1]

        result = []
        row, col = 0, -1
        direction = 0

        while remaining[direction % 2] > 0:
            dr, dc = directions[direction]

            for _ in range(remaining[direction % 2]):
                row += dr
                col += dc
                result.append(matrix[row][col])

            remaining[direction % 2] -= 1
            direction = (direction + 1) % 4

        return result