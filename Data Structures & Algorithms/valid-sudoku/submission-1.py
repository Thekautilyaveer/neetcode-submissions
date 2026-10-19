class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        width = len(board[0])
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(length):
            row = set()
            for j in range(width):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])


                grid_no = (i//3, j//3)
                if board[i][j] in boxes[grid_no]:
                    return False
                else:
                    boxes[grid_no].add(board[i][j])
        return True


        



