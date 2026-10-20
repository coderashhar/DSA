class Solution: 
    def helper(self, idx, s, lst, ans, n):
        if idx == n:
            ans.append(lst[:])
            return
        for i in range(idx, n):
            substr = s[idx : i+1]
            if substr == substr[::-1]:
                lst.append(substr)
                self.helper(i+1, s, lst, ans, n)
                lst.pop()
        
    def partition(self, s: str):
        lst = []
        ans = []
        self.helper(0, s, lst, ans, len(s))
        return ans