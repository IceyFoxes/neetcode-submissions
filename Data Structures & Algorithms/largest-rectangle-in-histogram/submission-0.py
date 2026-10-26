class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            height = heights[i]
            start = i
            
            while stack and height < stack[-1][0]:
                popped_height, popped_index = stack.pop()
                max_area = max(max_area, popped_height * (i - popped_index))
                start = popped_index

            stack.append((height, start))
        
        while stack:
            height, start = stack.pop()
            area = ((len(heights) - 1) - start + 1) * height
            max_area = max(area, max_area)

        return max_area
