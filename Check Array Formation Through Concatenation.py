class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in hashmap or len(arr) - i < len(hashmap[arr[i]]) or arr[i: i+len(hashmap[arr[i]])] != hashmap[arr[i]]:
                return False
            i += len(hashmap[arr[i]])
        return True
# Runtime: 44 ms, faster than 54.82% of Python3 online submissions for Check Array Formation Through Concatenation.
# Memory Usage: 14.3 MB, less than 12.34% of Python3 online submissions for Check Array Formation Through Concatenation.
