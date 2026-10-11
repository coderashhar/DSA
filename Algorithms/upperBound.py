class Solution:
    def upperbound_helper(self, nums, x, low, high, ans) -> int:
        if low > high:
            return ans
        mid = (low + high) // 2
        if nums[mid] > x:
            ans = min(mid, ans)
            high = mid - 1
            return self.upperbound_helper(nums, x, low, high, ans)
        elif nums[mid] <= x:
            low = mid + 1
            return self.upperbound_helper(nums, x, low, high, ans)

    def upperBound(self, nums, x):
        low = 0
        high = len(nums) - 1
        ans = len(nums)
        return self.upperbound_helper(nums, x, low, high, ans)
        