class Solution:   
    def helper(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n % 2 == 0:
            return self.helper(x * x, n // 2)
        return x * self.helper(x, n - 1)

    def myPow(self, x, n):
        num = n
        if num < 0:
            return 1.0 / self.helper(x, -num)
        return self.helper(x, num)
