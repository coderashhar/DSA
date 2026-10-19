class Solution:
    def helper(self, idx, nums, k, ans, lst, n):
        if sum(lst) > k:
            return
        if sum(lst) == k:
            ans.append(lst[:])
            return
        if idx == n:
            return

        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            lst.append(nums[i])
            self.helper(i+1, nums, k, ans, lst, n)
            lst.pop()

    def combinationSum2(self, candidates, target):
        ans = []
        lst = []
        candidates.sort()
        self.helper(0, candidates, target, ans, lst, len(candidates))
        return ans