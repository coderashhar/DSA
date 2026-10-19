class Solution:
    def helper(self, idx, nums, res, lst, n):
        if idx == n:
            res.append(lst[:])
            return 

        self.helper(idx+1, nums, res, lst, n)

        lst.append(nums[idx])
        self.helper(idx+1, nums, res, lst, n)
        lst.pop()
        
    def powerSet(self, nums):
        res = []
        lst = []
        n = len(nums)
        self.helper(0, nums, res, lst, n)
        return res