class Solution:
    def helper(self, idx, k, n, lst, ans):
        if sum(lst) == n and len(lst) == k:
            ans.append(lst[:])
            return
        if idx == 10:
            return 
        self.helper(idx+1, k, n, lst, ans)

        lst.append(idx)
        self.helper(idx+1, k, n, lst, ans)
        lst.pop()

    def combinationSum3(self, k, n):
        lst = []
        ans = []
        self.helper(1, k, n, lst, ans)
        return ans