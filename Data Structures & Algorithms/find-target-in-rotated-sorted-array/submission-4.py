class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            def check(index):
                return nums[index - 1] > nums[index]
            
            low = 0
            high = len(nums) - 1

            if len(nums) == 1:
                return 0

            while low <= high:
                mid = low + (high - low) // 2
                num = nums[mid]

                if check(mid):
                    return mid
                elif num > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        centre = findMin(nums)
        num = nums[centre]
        if target == num:
            return centre
        elif target <= nums[-1]:
            high = len(nums) - 1
            low = min(high, centre + 1)
        else:
            low = 0
            high = max(low, centre - 1)
        
        while low <= high:
            mid = low + (high - low) // 2
            print(low, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
                