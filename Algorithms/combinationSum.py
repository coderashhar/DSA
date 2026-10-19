class Solution:
    def helper(self, idx, nums, k, ans, lst, n):
        if sum(lst) > k:
            return
        if sum(lst) == k:
            ans.append(lst[:])
            return
        if idx == n:
            return 

        self.helper(idx+1, nums, k, ans, lst, n)

        lst.append(nums[idx])
        self.helper(idx, nums, k, ans, lst, n)
        lst.pop()
        
    def combinationSum(self, candidates, target):
        ans = []
        lst = []
        self.helper(0, candidates, target, ans, lst, len(candidates))
        return ans