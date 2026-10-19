class Solution:
    def helper(self, idx, nums, ans, sm, n):
        if idx == n:
            ans.append(sm)
            return
        
        self.helper(idx+1, nums, ans, sm, n)
        self.helper(idx+1, nums, ans, sm+nums[idx], n)
        

    def subsetSums(self, nums):
        ans = []
        sm = 0
        self.helper(0, nums, ans, sm, len(nums))
        return ans