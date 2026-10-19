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


                if i <=2 and j <= 2:
                    grid_no = 1
                elif i <= 2 and j <= 5:
                    grid_no = 2
                elif i <= 2 and j <= 8:
                    grid_no = 3

                elif i <=5 and j <= 2:
                    grid_no = 4
                elif i <= 5 and j <= 5:
                    grid_no = 5
                elif i <= 5 and j <= 8:
                    grid_no = 6

                elif i <=8 and j <= 2:
                    grid_no = 7
                elif i <= 8 and j <= 5:
                    grid_no = 8
                elif i <= 8 and j <= 8:
                    grid_no = 9

                if board[i][j] in boxes[grid_no]:
                    return False
                else:
                    boxes[grid_no].add(board[i][j])
        return True


        



