class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        start = 0
        res = 0

        for i in range(len(nums)):
            number = nums[i]
            product *= number

            while product >= k and start <= i:
                product /= nums[start]
                start += 1
            res += i - start + 1

        return res