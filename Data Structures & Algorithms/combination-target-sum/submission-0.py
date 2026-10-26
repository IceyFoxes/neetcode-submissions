class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # store ([nums], count) in a List
        combinations = []

        def addNumber(selectedNumber, target, index, combination):
            if selectedNumber > target:
                return

            target -= selectedNumber
            combination.append(selectedNumber)
            
            if target > 0:
                for i in range(index, len(nums)):
                    addNumber(nums[i], target, i, combination.copy())
            else:
                combinations.append(combination)
        
        for index in range(len(nums)):
            addNumber(nums[index], target, index, [])
        
        return combinations

            