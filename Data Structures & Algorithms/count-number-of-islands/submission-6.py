class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        res = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        def dfs(i,j):

            if (i,j) in seen:
                return
            seen.add((i,j))
            grid[i][j] = "0"
            for a,b in directions:
                new_i = i+a
                new_j = j+b
                if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols and (new_i, new_j) not in seen and grid[new_i][new_j] == "1":
                    
                    dfs(new_i, new_j)
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res+=1
        
        return res


        