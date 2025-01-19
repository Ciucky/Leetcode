class Solution:
    from heapq import heappush, heappop
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0 # A grid smaller than 3x3 cannot trap water

        # Min-heap to store boundary cells
        heap = []
        # Instead of a set, reuse the heightMap to mark visited cells by setting them to -1
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1 # Mark as visited

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water_trapped = 0
        max_height = 0

        while heap:
            height, x, y = heappop(heap)
            max_height = max(max_height, height)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heightMap[nx][ny] != -1:
                    # If the neighbor is not visited
                    trapped = max(0, max_height - heightMap[nx][ny])
                    water_trapped += trapped
                    # Push the neighbor into the heap with updated height
                    heappush(heap, (max(heightMap[nx][ny], max_height), nx, ny))
                    # Mark as visited
                    heightMap[nx][ny] = -1

        return water_trapped
