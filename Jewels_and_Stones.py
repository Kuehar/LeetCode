"""
https://leetcode.com/problems/jewels-and-stones/
"""

"""
Runtime:28ms
Memory:12.7MB
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        jewels = list(J)
        stones = list(S)
        for i in stones:
            if i in jewels:
                count += 1
        return count