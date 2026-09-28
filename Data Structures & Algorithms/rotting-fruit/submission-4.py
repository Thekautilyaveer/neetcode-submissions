class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        seen = set()
        fresh = 0

        def addnum(a, b):
            if a<0 or b<0 or a>= rows or b>= cols or (a,b) in seen or grid[a][b] == 0:
                return
            nonlocal fresh
            fresh-=1
            q.append([a,b])
            seen.add((a,b))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                    seen.add((i,j))
                if grid[i][j]== 1:
                    fresh+=1
        time = 0
        while q and fresh != 0:
            for i in range(len(q)):
                a, b = q.popleft()
                if grid[a][b] == 1:
                    grid[a][b] = 2


                addnum(a+1, b)
                addnum(a-1, b)
                addnum(a, b+1)
                addnum(a, b-1)
            time+=1
        if fresh != 0:
            return -1
        return time

        
                




            
