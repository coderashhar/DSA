class Solution:
    def helper(self, nums, target, low, high, ans) -> int:
        if low > high:
            return ans
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid 
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                return self.helper(nums, k, low, mid - 1, ans)
            else:
                return self.helper(nums, k, mid + 1, high, ans)
        else:
            if nums[mid] <= target <= nums[high]:
                return self.helper(nums, k, mid + 1, high, ans)
            else: 
                return self.helper(nums, k, low, mid - 1, ans)


    def search(self, nums, k):
        low = 0
        high = len(nums) - 1
        ans = -1
        return self.helper(nums, k, low, high, ans)

