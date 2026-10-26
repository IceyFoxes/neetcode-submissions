class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        permutations = []
        path = []

        def backtrack(candidates):
            if len(candidates) == 0:
                permutations.append(path.copy())
                return

            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack(candidates[: i] + candidates[i + 1 :])
                path.pop()

        backtrack(nums)
        return permutations