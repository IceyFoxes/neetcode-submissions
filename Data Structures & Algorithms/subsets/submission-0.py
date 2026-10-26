class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetList = [[]]
        for num in nums:
            for subset in subsetList.copy():
                subsetList.append(subset + [num])

        return subsetList