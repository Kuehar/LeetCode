class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= num:
                candies[i] = True
            else:
                candies[i] = False
        return candies
# Runtime: 64 ms, faster than 33.33% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num = max(candies)
        return [candy + extraCandies >= num for candy in candies]
# Runtime: 48 ms, faster than 33.33% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.