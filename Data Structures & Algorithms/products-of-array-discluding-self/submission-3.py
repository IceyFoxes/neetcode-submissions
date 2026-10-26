class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Setup prefix
        product = 1
        res = [1]
        for i in range(len(nums) - 1):
            product *= nums[i]
            res.append(product)

        # Multiply prefix and suffix for each
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix_product
            suffix_product *= nums[i]
        return res

