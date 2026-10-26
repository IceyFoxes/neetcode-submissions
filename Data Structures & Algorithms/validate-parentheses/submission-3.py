class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open = ('(', '[', '{')
        dict = { ')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if not stack:
                    return False
                match = stack.pop()
                if dict[char] != match:
                    return False
        
        return not stack

