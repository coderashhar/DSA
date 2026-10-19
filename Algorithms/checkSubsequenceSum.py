class Solution:
    def helper(self, idx, nums, sm, k, n):
        if sm == k:
            return True
        if idx == n:
            return False
        
        return self.helper(idx+1, nums, sm, k, n) or self.helper(idx+1, nums, sm+nums[idx], k, n)
        
    def checkSubsequenceSum(self, nums, k):
        sm = 0
        return self.helper(0, nums, sm, k, len(nums))
        