class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        path = []

        candidates.sort()
        def backtrack(start, remaining):
            if remaining == 0:
                combinations.append(path.copy())
                return
            
            prev = 0
            for i in range(start + 1, len(candidates)):
                if candidates[i] > remaining or prev == candidates[i]:
                    continue
            
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()
                prev = candidates[i]
        
        backtrack(-1, target)

        return combinations
