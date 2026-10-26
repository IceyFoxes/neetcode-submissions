class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # Count characters into a fixed-length 26-tuple
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # ✅ hashable, constant size
            anagrams[key].append(word)
        return list(anagrams.values())