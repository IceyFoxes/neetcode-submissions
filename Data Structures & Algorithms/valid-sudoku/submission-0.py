class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValid(item):
            return len(item) == len(set(item))

        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':  # skip empty cells
                    box_index = (i // 3) * 3 + (j // 3)
                    boxes[box_index].append(val)
                    column_index = j
                    columns[column_index].append(val)
                    row_index = i
                    rows[row_index].append(val)
        
        for box in boxes:
            if not isValid(box):
                return False
        for row in rows:
            if not isValid(row):
                return False
        for col in columns:
            if not isValid(col):
                return False
        
        return True


        