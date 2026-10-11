class Solution:
    def lowerbound_helper(self, nums, x, low, high, ans):
        if low > high:
            return ans
        mid = (low + high) // 2
        if nums[mid] >= x:
            ans = min(mid, ans)
            high = mid - 1
            return self.lowerbound_helper(nums, x, low, high, ans)
        elif nums[mid] < x:
            low = mid + 1
            return self.lowerbound_helper(nums, x, low, high, ans)


    def lowerBound(self, nums, x):
        low = 0
        ans = len(nums)
        high = len(nums) - 1
        return self.lowerbound_helper(nums, x, low, high, ans)


