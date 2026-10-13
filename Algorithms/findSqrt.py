class Solution:
    def floorSqrt(self, n: int) -> int:
        low = 0
        high = n
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            sq = mid ** 2
            if sq == n:
                return mid
            elif sq < n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans