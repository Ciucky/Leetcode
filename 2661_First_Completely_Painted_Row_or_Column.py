class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m # Track painted cells in each row
        col_count = [0] * n # Track painted cells in each column
        num_to_position = {} # Map numbers to their (row, col) positions

        # Precompute the positions of each number in the grid
        for i in range(m):
            for j in range(n):
                num_to_position[mat[i][j]] = (i, j)

        # Process each number in the given order
        for index, num in enumerate(arr):
            if num in num_to_position:
                x, y = num_to_position[num]
                row_count[x] += 1
                col_count[y] += 1

                # Check if the row or column is completely painted
                if row_count[x] == n or col_count[y] == m:
                    return index

        return -1 # Should never reach here
