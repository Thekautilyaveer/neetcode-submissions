class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        seen = set()
        distance = [[1,0], [0,1], [-1,0], [0,-1]]

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
                for a, b in distance:
                    ni = i+a
                    nj = j+b
                    if ni >= rows or ni < 0 or nj >= cols or nj < 0 or grid[ni][nj] == -1 or (ni, nj) in seen:
                        continue
                    seen.add((ni,nj))
                    q.append([ni, nj])



            dist+=1


        