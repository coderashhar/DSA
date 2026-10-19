class Solution:
    def countSum(self, a, k):
        n = len(a)
        ans = 1
        sm = 0
        for i in range(n):
            if sm + a[i] <= k:
                sm += a[i]
            else:
                ans += 1
                sm = a[i]
        return ans
        
    def largestSubarraySumMinimized(self, a, k):
        n = len(a)
        if k > n:
            return -1
        low = max(a)
        high = sum(a)
        while low <= high:
            mid = (low + high) // 2
            ans = self.countSum(a, mid)
            if ans > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
