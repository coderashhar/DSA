class Solution:
    def helper(self, idx, digits, lst, ans, n, keypad):
        if idx == n:
            res = "".join(lst)
            ans.append(res)
            return 
        for char in keypad[int(digits[idx])]:
            lst.append(char)
            self.helper(idx+1, digits, lst, ans, n, keypad)
            lst.pop()


    def letterCombinations(self, digits):
        keypad = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        lst = []
        ans = []
        n = len(digits)
        if n == 0:
            return ans
        self.helper(0, digits, lst, ans, n, keypad)
        return ans 
