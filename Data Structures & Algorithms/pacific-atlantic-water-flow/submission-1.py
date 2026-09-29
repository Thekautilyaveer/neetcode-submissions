class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q = collections.deque()
        atl_q = collections.deque()
        p_seen = set()
        atl_seen = set()
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        res= []

        rows = len(heights)
        cols = len(heights[0])

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    p_q.append((i,j))
                if i == rows-1 or j == cols-1:
                    atl_q.append((i,j))

        while p_q:
            a, b = p_q.popleft()
            if (a,b) not in p_seen:
                p_seen.add((a,b))
                for i, j in directions:
                    val = (a+i, b+j) 
                    if not (a+i < 0 or a+i >= rows or b+j < 0 or b+j >= cols or (a+i, b+j) in p_seen) and heights[a+i][b+j] >= heights[a][b]:
                        p_q.append((a+i, b+j))

        while atl_q:
            a, b = atl_q.popleft()
            if (a,b) not in atl_seen:
                atl_seen.add((a,b))
                for i, j in directions:
                    val = (a+i, b+j) 
                    if not (a+i < 0 or a+i >= rows or b+j < 0 or b+j >= cols or (a+i, b+j) in atl_seen) and heights[a+i][b+j] >= heights[a][b]:
                        atl_q.append((a+i, b+j))


        for (m, n) in p_seen & atl_seen:
            res.append([m, n])

        return res


                        
                    



            

        