class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # mとnが0になるまでループ。各処理の最後で該当する値をディクリメント。
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
# Runtime: 36 ms, faster than 74.64% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.3 MB, less than 33.67% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()
# Runtime: 146 ms, faster than 23.78% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.8 MB, less than 61.64% of Python3 online submissions for Duplicate Zeros.
