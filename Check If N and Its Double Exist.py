class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for a in arr:
            if a * 2 in seen or a / 2 in seen:
                return True
            seen.add(a)
        return False
# Runtime: 110 ms, faster than 10.92% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 14 MB, less than 96.65% of Python3 online submissions for Check If N and Its Double Exist.
