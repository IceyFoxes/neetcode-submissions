class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        letterCount = 0
        dictionary = defaultdict(int)
        res = 0

        while end < len(s):
            dictionary[s[end]] += 1
            letterCount = max(letterCount, dictionary[s[end]])
            while (end - start + 1) - letterCount > k:
                dictionary[s[start]] -= 1
                start += 1
            res = max(res, (end - start + 1))
            end += 1
        
        return res


