class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []
        placement = []
        colsTaken = set()
        diagonalsLeftTaken = set()
        diagonalsRightTaken = set()
        rows = ['.' * col + 'Q' + '.' * (n - 1 - col) for col in range(n)]

        def checkValid(row, col):
            # skip check horizontal since we are placing row by row
            # check vertical
            if col in colsTaken:
                return False
            # check diagonals
            if row + col in diagonalsLeftTaken:
                return False
            if row - col in diagonalsRightTaken:
                return False
            return True
        
        def placeQueen(row, col):
            colsTaken.add(col)
            diagonalsLeftTaken.add(row + col)
            diagonalsRightTaken.add(row - col)
            placement.append(rows[col])

        def removeQueen(row, col):
            colsTaken.remove(col)
            diagonalsLeftTaken.remove(row + col)
            diagonalsRightTaken.remove(row - col)
            placement.pop()

        # for each row, pick a spot
        def backtrack(row):
            if row == n:
                answers.append(placement.copy())
                return

            # how to pick a spot?
            # loop through all n spots, and check validity
            for col in range(n):
                # more than 1 spot?
                # backtrack
                if checkValid(row, col):
                    placeQueen(row, col)
                    backtrack(row + 1)
                    removeQueen(row, col)            
            return

        backtrack(0)
        # return possible answers
        return answers