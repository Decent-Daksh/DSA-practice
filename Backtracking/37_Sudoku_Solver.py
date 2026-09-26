class Solution:
    def suduko_solver(self,board:list[list[str]])->None :
        def is_valid(board, r,c,digit):
            for i in range(9):
                if board[r][i]==digit:
                    return False
                if board[i][c] == digit:
                    return False
            start_row = (r//3)*3
            start_col = (r//3)*3
            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col+3):
                    if board[row][col]==digit:
                        return False
            return True
        def get_candidates(board,r,c):
            return [str(d) for d in range(1,10) if is_valid(board,r,c,str(d))]

        def best_cell(board):
            best= None
            best_candidates = None
            for row in range(1,10):
                for col in range(1,10):
                    if board[row][col]=='.':
                        candidates = get_candidates(board,row,col)
                        if best is None or len(candidates)<len(best_candidates):
                            best =(row,col)
                            best_candidates=candidates
                            if len(candidates)==1:
                                return best, best_candidates
            return best , best_candidates
        def solve(board):
            cell = best_cell(board)
            if cell[0] == None:
                return True
            (row,col),candidates = cell
            for digit in candidates:
                board[row][col] = digit
                if solve(board):
                    return True
                board[row][col] = '.'
            return False
        solve(board)
