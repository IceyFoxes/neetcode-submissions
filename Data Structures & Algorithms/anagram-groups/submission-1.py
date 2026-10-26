class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = dict()
        for word in strs:
            counter = frozenset(Counter(word).items())
            if counter not in dictionary:
                dictionary[counter] = []
            dictionary[counter].append(word)
        
        return list(dictionary.values())