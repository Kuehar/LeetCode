"""
Runtime:28ms
Memory:12.9MB
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        total = 0
        for i in s:
            if i == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                total +=1
        return total
        
