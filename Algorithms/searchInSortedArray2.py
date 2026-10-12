class Solution:
    def helper(self, nums, k, low, high, ans) -> int:
        if low > high:
            return ans
        mid = (low + high) // 2
        if nums[mid] == k:
            return True 
        if nums[low] == nums[mid] == nums[high]:
            return self.helper(nums, k, low + 1, high - 1, ans)

        if nums[low] <= nums[mid]:
            if nums[low] <= k <= nums[mid]:
                return self.helper(nums, k, low, mid - 1, ans)
            else:
                return self.helper(nums, k, mid + 1, high, ans)
        else:
            if nums[mid] <= k <= nums[high]:
                return self.helper(nums, k, mid + 1, high, ans)
            else: 
                return self.helper(nums, k, low, mid - 1, ans)

    def searchInARotatedSortedArrayII(self, nums, k):
        low = 0
        high = len(nums) - 1
        ans = False
        return self.helper(nums, k, low, high, ans)