class Solution:
    def possiblePlacement(self, board, row, col, n):
        r, c = row, col
        while r >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
        r, c = row, col
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        return True

    def helper(self, row, board, ans, n):
        if row == n:
            solution = []
            for i in range(n):
                solution.append("".join(board[i]))
            ans.append(solution) 
            return  

        for col in range(0, n):
            if self.possiblePlacement(board, row, col, n):
                board[row][col] = 'Q'
                self.helper(row+1, board, ans, n)
                board[row][col] = '.'

    
    def solveNQueens(self, n):
        board = []
        ans = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
            board.append(row)
        self.helper(0, board, ans, n)
        return ans
