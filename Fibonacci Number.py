class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * 50

        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
        
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
