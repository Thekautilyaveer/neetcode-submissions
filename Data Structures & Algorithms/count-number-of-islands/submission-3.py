class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        directions = [[0,1], [1,0], [0, -1], [-1,0]]
        def bfs(i, j):
            q = collections.deque()
            q.append((i,j))
            while q:
                i, j = q.popleft()
                if i >= 0 and j >= 0 and i  <= len(grid)-1 and j <= len(grid[0])-1 and grid[i][j] == "1":

                    grid[i][j] = "0"

                    for dr, dc in directions:
                        if i+dr <= len(grid)-1 and j+dc <= len(grid[0])-1:
                            q.append((i+dr, j+dc))


        i, j = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num +=1
                    bfs(i, j)

        return num

