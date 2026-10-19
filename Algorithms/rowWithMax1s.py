class Solution:
    def countOnes(self, row):
        n = len(row)
        cnt = 0
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == 1:
                cnt = n - mid
                high = mid - 1
            else:
                low = mid + 1
        return cnt



                

    def rowWithMax1s(self, mat):
        n = len(mat)
        mx = 0
        mxrow = -1
        for i in range(n):
            cnt = self.countOnes(mat[i])
            if cnt > mx:
                mx = cnt
                mxrow = i
        return mxrow 
    