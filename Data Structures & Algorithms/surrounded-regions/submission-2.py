from _heapq import heapify
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        q= collections.deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    if board[i][j] == "O":
                        q.append([i, j])

        while q:
            for item in range(len(q)):
                r, c = q.popleft()
                seen.add((r,c))
                for a, b in directions:
                    nr = r+a
                    nc = c+b
                    if not (nr<0 or nc<0 or nr>= rows or nc >= cols or (nr, nc) in seen):
                        if board[nr][nc] == "O":
                            seen.add((nr, nc))
                            q.append([nr, nc])

        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen:
                    board[i][j] = "X"
                

        
        