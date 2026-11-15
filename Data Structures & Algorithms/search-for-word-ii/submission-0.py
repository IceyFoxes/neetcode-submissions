class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node["#"] = word

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        found = []

        def dfs(row, col, parent):
            if not (0 <= row < rows and 0 <= col < cols):
                return

            letter = board[row][col]
            if letter not in parent:
                return

            node = parent[letter]
            word = node.pop("#", None)
            if word is not None:
                found.append(word)

            board[row][col] = "*"
            for dr, dc in directions:
                dfs(row + dr, col + dc, node)
            board[row][col] = letter

            if not node:
                del parent[letter]

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return found