class Solution:
    def helper(self, idx, nums, k, sm, cnt, n):
        if sm == k:
            cnt += 1
            return cnt
        if idx == n:
            return cnt
        include = self.helper(idx+1, nums, k, sm+nums[idx], cnt, n)
        exclude = self.helper(idx+1, nums, k, sm, cnt, n)
        return include + exclude

    def countSubsequenceWithTargetSum(self, nums, k):
        sm = 0
        cnt = 0
        return self.helper(0, nums, k, sm, cnt, len(nums))