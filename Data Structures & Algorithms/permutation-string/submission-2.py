class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1) - 1
        target_freq = Counter(s1)
        freq = Counter(s2[: len(s1)])

        while right < len(s2):
            if freq == target_freq:
                return True

            if right == len(s2) - 1:
                return False
            right += 1
            freq[s2[right]] += 1
            freq[s2[left]] -= 1
            left += 1
        
        return False

        
        
