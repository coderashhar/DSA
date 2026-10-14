class Solution:
    def sumByD(self, nums, limit):
        n = len(nums)
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val

    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1
        return low