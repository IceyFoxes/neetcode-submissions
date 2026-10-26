class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        target_freq = Counter(s1)
        freq = Counter(s2[: len(s1)])
        if freq == target_freq:
            return True
        
        for index in range(len(s1), len(s2)):
            # shifting the window
            right_char = s2[index]
            left_char = s2[index - len(s1)]
            
            # updating the freqs
            freq[right_char] += 1
            freq[left_char] -= 1

            if freq[left_char] == 0:
                del freq[left_char]
                
            if freq == target_freq:
                return True
        
        return False

        
        
