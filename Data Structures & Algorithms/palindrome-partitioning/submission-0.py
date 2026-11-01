class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []
        path = []

        def backtrack(idx):
            if idx == len(s):
                substrings.append(path.copy())
                return

            for end in range(idx + 1, len(s) + 1):
                candidate = s[idx:end]

                if candidate == candidate[::-1]:
                    path.append(candidate)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return substrings

