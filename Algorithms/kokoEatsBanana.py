class Solution:
    def sumByD(self, nums, h):
        n = len(nums)
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / h)
        return sum_val

    def minimumRateToEatBananas(self, nums, h):
        n = len(nums)
        if n > h:
            return -1
        
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low