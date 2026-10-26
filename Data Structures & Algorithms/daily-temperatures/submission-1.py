class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]

        stack = []

        for index in range(len(temperatures) - 1, -1, -1):
            temperature = temperatures[index]
            if not stack:
                stack.append(index)
                # res[index] = 0
            else:
                while stack and temperature >= temperatures[stack[-1]]:
                    stack.pop()
                
                if stack:
                    res[index] = stack[-1] - index
                stack.append(index)
        
        return res


