class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = dict()
        start = 0
        maxLength = 0

        letters = list(s)
        for index in range(len(letters)):
            letter = letters[index]
            
            if letter in res and res[letter] >= start:
                start = res[letter] + 1
            
            res.update({letter : index})
            maxLength = max(maxLength, (index - start + 1))
        
        return maxLength