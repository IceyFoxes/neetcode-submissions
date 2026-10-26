class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = dict()
        start = 0
        maxLength = 0

        for index, letter in enumerate(s):
            if letter in res and res[letter] >= start:
                start = res[letter] + 1
            
            res[letter] = index
            maxLength = max(maxLength, (index - start + 1))
        
        return maxLength