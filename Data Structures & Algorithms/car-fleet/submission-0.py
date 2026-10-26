class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        helper = sorted(zip(position, speed))
        helper.sort()

        i = len(helper) - 1
        car_fleet = 0

        # the first car of a fleet
        while i >= 0:
            car_position = helper[i][0]
            car_speed = helper[i][1]
            time = (target - car_position) / car_speed
            i -= 1

        # now check how many other cars are in the fleet
            while i >= 0:
                car_position = helper[i][0]
                car_speed = helper[i][1]
                # reached target (we can break upon the first car which doesn't. it's the next fleet)
                if car_position + car_speed * time < target:
                    break
                i -= 1
            
            car_fleet += 1
        
        return car_fleet