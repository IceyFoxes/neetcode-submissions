class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        low = 0
        high = len(nums1)

        while low <= high:
            i = low + (high - low) // 2
            j = half - i

            # The elements to the left of the partition
            nums1Left = nums1[i - 1] if i > 0 else float('-infinity')
            nums2Left = nums2[j - 1] if j > 0 else float('-infinity')

            # The elements to the right of the partition
            nums1Right = nums1[i] if i < len(nums1) else float('infinity')
            nums2Right = nums2[j] if j < len(nums2) else float('infinity')
            
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total_length % 2 == 1:
                    return min(nums1Right, nums2Right)
                else:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2

            elif nums1Left > nums2Right:
                high = i - 1

            else:
                low = i + 1
            

                
