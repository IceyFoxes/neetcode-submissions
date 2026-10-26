class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        path = []

        def backtrack(n, unmatched):
            if n == 0:
                combinations.append(''.join(path))
                return
            
            if n > unmatched:
                path.append('(')
                backtrack(n, unmatched + 1)
                path.pop()

            if unmatched > 0:
                path.append(')')
                backtrack(n - 1, unmatched - 1)
                path.pop()

        backtrack(n, 0)
        return combinations

