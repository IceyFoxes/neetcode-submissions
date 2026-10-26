class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = dict()
        res = 0
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] in dictionary and dictionary[s[i]] >= start:
                start = dictionary[s[i]] + 1
            
            end = i
            dictionary[s[i]] = i
            length = end - start + 1
            res = max(length, res)
        return res