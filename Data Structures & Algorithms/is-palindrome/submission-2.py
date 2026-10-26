class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        mid = len(s) // 2

        if len(s) % 2 == 0:
            return s[:mid] == s[len(s) - 1:mid - 1:-1]
        else:
            return s[:mid] == s[len(s) - 1:mid:-1]
            