class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Setup prefix
        res = 1
        prefix = [1]
        for i in nums:
            res *= i
            prefix.append(res)
        
        res = 1
        nums_reverse = nums[::-1]
        suffix = deque([1])
        for i in nums_reverse:
            res *= i
            suffix.appendleft(res)

        # Multiply prefix and suffix for each
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i + 1])
        return res

