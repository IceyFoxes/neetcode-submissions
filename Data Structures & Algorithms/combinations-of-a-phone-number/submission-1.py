class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        combination = []
        letterMapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def backtrack(idx):
            if idx == len(digits):
                combinations.append(''.join(combination))
                return

            for letter in letterMapping[digits[idx]]:
                combination.append(letter)
                backtrack(idx + 1)
                combination.pop()

        if digits:
            backtrack(0)
        return combinations