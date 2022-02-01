class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        i = len(arr)-1
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i -=1
        return arr
# Runtime: 169 ms, faster than 57.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 15.2 MB, less than 97.02% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
