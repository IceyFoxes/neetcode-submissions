class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # store ([nums], count) in a List
        combinations = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                combinations.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    continue
                
                path.append(nums[i])
                backtrack(i, remaining - nums[i])
                path.pop()
        
        backtrack(0, target)
        return combinations

            