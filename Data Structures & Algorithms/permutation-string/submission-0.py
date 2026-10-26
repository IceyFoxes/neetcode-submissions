class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            counter2 = Counter(s2[i:i + len(s1)])
            if counter1 == counter2:
                return True

        return False
        