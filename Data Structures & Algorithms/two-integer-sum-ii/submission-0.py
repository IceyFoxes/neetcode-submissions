class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Sliding window

        low = 0
        high = len(numbers) - 1

        while low < high:
            sums = numbers[low] + numbers[high]

            if sums == target:
                return [low + 1, high + 1]
            elif sums < target:
                low += 1
            else:
                high -= 1
        

        
