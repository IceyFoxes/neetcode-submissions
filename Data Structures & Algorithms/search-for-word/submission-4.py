class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def backtrack(row, col, index):
            if not (0 <= row < rows and 0 <= col < cols):
                return False
            if (row, col) in seen:
                return False
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            seen.add((row, col))

            found = any(
                backtrack(row + dr, col + dc, index + 1)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            )

            seen.remove((row, col))
            return found

        return any(
            backtrack(row, col, 0)
            for row in range(rows)
            for col in range(cols)
        )
        