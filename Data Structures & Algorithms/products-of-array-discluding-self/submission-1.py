class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        # prefix[i] = product of nums[0] to nums[i - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # suffix[i] = product of nums[i + 1] to nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # result = prefix[i] * suffix[i]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res