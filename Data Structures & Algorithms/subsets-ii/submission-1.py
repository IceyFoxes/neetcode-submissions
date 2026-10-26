class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        path = []

        def backtrack(start):
            subsets.append(path.copy())
            prev = None
            for i in range(start + 1, len(nums)):
                if nums[i] == prev:
                    continue
                path.append(nums[i])
                backtrack(i)
                path.pop()
                prev = nums[i]
        
        backtrack(-1)
        return subsets






