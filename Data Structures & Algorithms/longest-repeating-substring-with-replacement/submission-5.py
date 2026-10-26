class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        right = 0
        max_freq = 0
        max_length = 0

        while right < len(s):
            
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            letters = right - left + 1
            if letters > max_freq + k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
        

