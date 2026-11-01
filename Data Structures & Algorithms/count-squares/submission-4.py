class CountSquares:

    def __init__(self):
        # point : count
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        query_x, query_y = point
        counts = 0

        for (x, y), diagonal_count in self.points.items():
            if x == query_x or abs(x - query_x) != abs(y - query_y):
                continue

            counts += (
                diagonal_count
                * self.points.get((x, query_y), 0)
                * self.points.get((query_x, y), 0)
            )

        return counts
        


