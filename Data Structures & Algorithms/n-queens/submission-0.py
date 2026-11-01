class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []
        placement = []
        queens = []

        def checkValid(row, col):
            # skip check horizontal since we are placing row by row
            # check vertical
            for queen in queens:
                if queen[1] == col:
                    return False
                if abs(queen[0] - row) == abs(queen[1] - col):
                    return False
            return True
        
        def placeQueen(row, col):
            queens.append((row, col))
            position = '.' * col + 'Q' + '.' * (n - 1 - col)
            placement.append(position)

        def removeQueen(row, col):
            queens.pop()
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