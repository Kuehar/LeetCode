class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,1+n):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
# Runtime: 36 ms, faster than 92.53% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.9 MB, less than 71.40% of Python3 online submissions for Fizz Buzz.
