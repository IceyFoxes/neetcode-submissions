class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # dictionary to store highest seen index for each character
        char_pos = dict()

        # at each duplicate char, record the curr length (compared to max) --> keep a count of length
        max_length = 0
        start = 0

        for i in range(len(s)):
            char = ord(s[i])
            if char in char_pos:
                start = max(char_pos[char] + 1, start)
            
            # then update the dictionary with the new higher index
            char_pos[char] = i
            max_length = max(max_length, i - start + 1)
    
        return max_length
