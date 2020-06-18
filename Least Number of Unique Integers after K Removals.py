import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        sorted_counts,removed_counts = sorted(Counter(arr).items(),key=lambda x: x[1]),0
        for keys,values in sorted_counts:
            if k >= values:
                k -= values
                removed_counts += 1
        return len(sorted_counts) - removed_counts

# Runtime: 496 ms, faster than 92.08% of Python3 online submissions for Least Number of Unique Integers after K Removals.
# Memory Usage: 32.9 MB, less than 33.33% of Python3 online submissions for Least Number of Unique Integers after K Removals.
