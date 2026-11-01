class Solution:
    def helper(self, row, col, grid, path, ans, n):
        if row == n-1 and col == n-1:
            ans.append("".join(path))
            return

        # Mark current cell as visited
        grid[row][col] = 0

        # Directions: D, L, R, U
        directions = [
            (1, 0, 'D'),
            (0, -1, 'L'),
            (0, 1, 'R'),
            (-1, 0, 'U')
        ]

        for dr, dc, move in directions:
            nr = row + dr
            nc = col + dc

            if (0 <= nr < n and
                0 <= nc < n and
                grid[nr][nc] == 1):

                path.append(move)

                self.helper(nr, nc, grid, path, ans, n)

                # Backtrack
                path.pop()

        # Restore current cell
        grid[row][col] = 1

    def findPath(self, grid):
        n = len(grid)
        ans = []
        if grid[0][0] == '0':
            return [-1]
        self.helper(0, 0, grid, [], ans, n)
        if not ans:
            return -1
        return sorted(ans)
