class Solution:
    def trap(self, height: List[int]) -> int:
        
        index = 0
        total_water = 0
        left = 0
        right = len(height) - 1
        water_height = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            new_height = min(left_height, right_height)
            
            if new_height > water_height:
                water_height = new_height
            
            total_water += max(0, (water_height - min(left_height, right_height)))
            
            if left_height > right_height:
                right -= 1
            else:
                left += 1
        
        return total_water

        

