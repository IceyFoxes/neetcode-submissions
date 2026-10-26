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
        max_length = 0
        res = (0, 0)

        for right in range(len(s)):
            counter[s[right]] += 1
            
            while contains(counter, t_counter):
                length = right - left + 1
                if length < max_length or res == (0, 0):
                    res = (left, right + 1)
                    max_length = length
                counter[s[left]] -= 1
                left += 1

        return s[res[0] : res[1]]


