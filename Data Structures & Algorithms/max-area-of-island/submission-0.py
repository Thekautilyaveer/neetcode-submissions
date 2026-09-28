class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0

        def dfs(i, j):
            if i >=rows or j >= cols or i< 0 or  j < 0 or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            ar = 1
            for ir,jr in directions:
                    ar+= dfs(i+ir, j + jr)
            
            return ar

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i,j))

        return maxarea
        