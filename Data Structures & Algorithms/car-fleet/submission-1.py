class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair them up and sort in reverse (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            
            # If the car behind catches up to the car ahead, they merge!
            # We pop the faster car's time because the fleet moves at the slower car's time.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # The number of remaining independent times is the number of fleets
        return len(stack)