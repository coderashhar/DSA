class Solution:
    def helper(self, idx, st, op, cl, lst, n):
        if op > n: 
            return
        if op + cl == 2*n and op == cl:
            lst.append(st)
            return
        if op < n:
            self.helper(idx+1, st+"(", op+1, cl, lst, n)
        if op > cl:
            self.helper(idx+1, st+")", op, cl+1, lst, n)

    def generateParenthesis(self, n):
        lst = []
        self.helper(0, "", 0, 0, lst, n)
        return lst