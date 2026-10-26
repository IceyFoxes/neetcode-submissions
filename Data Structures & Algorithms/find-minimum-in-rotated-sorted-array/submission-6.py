class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the point where its left neighbour > itself

        def check(index):
            return nums[index - 1] > nums[index]
        
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while low <= high:
            mid = low + (high - low) // 2
            print(mid)
            num = nums[mid]

            if check(mid):
                return num
            elif num > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                