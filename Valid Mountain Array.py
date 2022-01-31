class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m = max(arr)
        is_passed = False
        
        if len(arr) < 3 or arr[-1] == m:
            return False
        
        
        for i in range(1,len(arr)):
            if is_passed:
                if arr[i-1] <= arr[i]:
                    return False
            else:
                if arr[i-1] >= arr[i]:
                    return False
            if arr[i] == m:
                is_passed = True
        return True
# Runtime: 204 ms, faster than 82.97% of Python3 online submissions for Valid Mountain Array. O(N)
# Memory Usage: 15.5 MB, less than 61.57% of Python3 online submissions for Valid Mountain Array.
