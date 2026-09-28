class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        directions = [[0,1], [1,0], [0, -1], [-1,0]]
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"

            for dr, dc in directions:
                dfs(i+dr, j+dc)


        i, j = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num +=1
                    dfs(i, j)

        return num

