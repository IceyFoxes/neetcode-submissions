class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = []
        seen = set()

        def backtrack(n, row, col):
            if n == 0:
                return ''.join(path) == word
            
            for i, j in moves(row, col):
                if (i, j) in seen:
                    continue

                path.append(board[i][j])
                seen.add((i, j))
                found = backtrack(n - 1, i, j)
                path.pop()
                seen.remove((i, j))

                if found:
                    return True
        
        def moves(row, col):
            actions = []
            if row - 1 >= 0 and (row - 1, col) not in seen:
                actions.append((row - 1, col))
            if row + 1 < len(board) and (row + 1, col) not in seen:
                actions.append((row + 1, col))
            if col - 1 >= 0 and (row, col - 1) not in seen:
                actions.append((row, col - 1))
            if col + 1 < len(board[row]) and (row, col + 1) not in seen:
                actions.append((row, col + 1))      
            return actions    
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                path.append(board[row][col])
                seen.add((row, col))
                if backtrack(len(word) - 1, row, col):
                    return True
                path.pop()
                seen.remove((row, col))

        return False
        