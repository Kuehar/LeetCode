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

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        cache = [0]*(n+1)
        cache[1] = 1
        for i in range(2,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
# Runtime: 28 ms, faster than 85.51% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 97.87% of Python3 online submissions for Fibonacci Number.    
