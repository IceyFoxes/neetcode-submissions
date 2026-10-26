class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        combinations = []
        path = []
        openBrackets = 0

        def backtrack(n):
            nonlocal openBrackets
            if n == 0:
                combinations.append(''.join(path))
                return
            
            if n > openBrackets:
                openBrackets += 1
                path.append('(')
                backtrack(n)
                path.pop()
                openBrackets -= 1

            if openBrackets > 0:
                openBrackets -= 1
                path.append(')')
                backtrack(n - 1)
                path.pop()
                openBrackets += 1

        backtrack(n)
        return combinations

