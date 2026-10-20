class Solution:
    def helper(self, idx, i, j, board, word, n, m):
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        c = board[i][j]
        board[i][j] = ""
        ans = ( self.helper(idx+1, i-1, j, board, word, n, m) or 
                self.helper(idx+1, i+1, j, board, word, n, m) or 
                self.helper(idx+1, i, j-1, board, word, n, m) or 
                self.helper(idx+1, i, j+1, board, word, n, m)
            )
        board[i][j] = c
        return ans

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(0, i, j, board, word, n, m):
                    return True
        return False