class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[-i - 1])
        suffix = suffix[::-1]
        
        res = [suffix[0]]
        for i in range(1, len(nums) - 1):
            res.append(prefix[i - 1] * suffix[i])
        res.append(prefix[-1])

        return res