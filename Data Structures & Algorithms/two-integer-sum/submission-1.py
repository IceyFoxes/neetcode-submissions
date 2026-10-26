class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {number: index for index, number in enumerate(nums)}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictionary and dictionary[diff] != i:
                return [i, dictionary[diff]]