class CountSquares:

    def __init__(self):
        # point : count
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # for any pair of coordinates on the x, y-axis (points), try to find if it exists as a point
        x_axis = defaultdict(int)
        y_axis = defaultdict(int)
        for otherPoint in self.points:
            if otherPoint == tuple(point):
                continue
            if otherPoint[0] == point[0]:
                y_axis[otherPoint[1]] += self.points[otherPoint]
            if otherPoint[1] == point[1]:
                x_axis[otherPoint[0]] += self.points[otherPoint]

        counts = 0
        for x, count_x in x_axis.items():
            for y, count_y in y_axis.items():
                if abs(x - point[0]) == abs(y - point[1]):
                    counts += self.points.get((x, y), 0) * count_x * count_y
        return counts
        


