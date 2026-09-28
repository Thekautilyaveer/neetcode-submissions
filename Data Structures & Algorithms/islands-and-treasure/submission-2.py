class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        seen = set()


        def addVal (i, j):
            if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == -1 or (i, j) in seen:
                return 
            seen.add((i,j))
            q.append([i, j])
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    seen.add((i,j))

        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addVal(i, j+1)
                addVal(i, j-1)
                addVal(i+1, j)
                addVal(i-1, j)

            dist+=1


        