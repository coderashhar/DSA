class Solution:
    def targetPresent(self, row, target) -> bool:
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, mat, target):
        for row in mat:
            ans = self.targetPresent(row, target)
            if ans == True:
                return True
        return False
    