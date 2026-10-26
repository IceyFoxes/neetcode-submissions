import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # quick select
        def quickselect(k, array):
            pivot = array[random.randint(0, len(array) - 1)]
            larger = []
            equal = []
            smaller = []
            
            for number in array:
                if number > pivot:
                    larger.append(number)
                elif number == pivot:
                    equal.append(number)
                else:
                    smaller.append(number)
            
            if len(larger) >= k:
                return quickselect(k, larger)
            elif len(larger) + len(equal) >= k:
                return pivot
            else:
                return quickselect(k - len(larger) - len(equal), smaller)

        return quickselect(k, nums)