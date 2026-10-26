class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def contains(count1, count2):
            for letter, count in count2.items():
                if count1[letter] < count:
                    return False
            return True
        
        left = 0
        counter = defaultdict(int)
        t_counter = Counter(t)
        have = 0
        need = len(t_counter)
        max_length = 0
        res = (0, 0)

        for right in range(len(s)):
            char = s[right]
            counter[char] += 1

            if char in t_counter and counter[char] == t_counter[char]:
                have += 1
            
            while have == need:
                length = right - left + 1
                if length < max_length or res == (0, 0):
                    res = (left, right + 1)
                    max_length = length
                
                left_char = s[left]
                counter[left_char] -= 1
                if left_char in t_counter and counter[left_char] < t_counter[left_char]:
                    have -= 1
                
                left += 1

        return s[res[0] : res[1]]


