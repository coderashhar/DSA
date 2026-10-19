class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        if n == m == 1:
            return [0,0]
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            mx = 0
            mxrow = 0
            for i in range(n):
                num = mat[i][mid]
                if num > mx:
                    mx = num
                    mxrow = i
            left = mat[mxrow][mid - 1] if mid-1 >= 0 else -1
            right = mat[mxrow][mid + 1] if mid+1 < m else -1
            if left < mat[mxrow][mid] and mat[mxrow][mid] > right:
                return [mxrow, mid]
            if mat[mxrow][mid] < mat[mxrow][mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]


