class Solution:
    def average(self, salary: List[int]) -> float:
        temp,low,high = 0,float('inf'),float('-inf')
        for s in salary:
            temp += s
            low,high = min(low,s),max(high,s)
        return (temp - low - high)/(len(salary)-2)
# Runtime: 36 ms, faster than 59.24% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)
# Runtime: 20 ms, faster than 99.36% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
