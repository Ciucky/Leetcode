class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # Total sums for both rows
        total_top = sum(grid[0])
        total_bottom = 0

        result = float('inf')

        # Iterate over each column where the robot can transition
        for i in range(n):
            # Points left for the second robot
            top_points = total_top - grid[0][i] # Remaining points in the top row
            bottom_points = total_bottom # Points accumulated in the bottom row

            # Second robot's strategy: maximize points they can get
            second_robot_points = max(top_points, bottom_points)

            # Minimize the first robot's forced score
            result = min(result, second_robot_points)

            # Update the bottom row's total as the first robot moves down
            total_bottom += grid[1][i]
            # Update the top row's total as the first robot moves across
            total_top -= grid[0][i]

        return result
