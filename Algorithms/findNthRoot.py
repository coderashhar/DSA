class Solution:
    def NthRoot(self, n, m):
        low = 0
        high = m
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            val = mid ** n
            if val == m:
                return mid
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1
        return ans      