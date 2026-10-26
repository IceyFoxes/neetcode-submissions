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
                if char not in dict or dict[char] != match:
                    return False
        
        if stack:
            return False
        return True

