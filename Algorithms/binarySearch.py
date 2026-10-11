class Solution:
    def binary_search(self, nums, target, low, high) -> int:
        mid = (low + high) // 2
        if low > high:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
            return self.binary_search(nums, target, low, high)
        else:
            high = mid - 1
            return self.binary_search(nums, target, low, high)


    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        return self.binary_search(nums, target, low, high)

