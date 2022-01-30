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
# Runtime: 40 ms, faster than 62.01% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14 MB, less than 94.01% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copied_nums1 = nums1[:m]
        
        p1 = p2 = 0
        for p in range(n+m):
            if p2 >= n or (p1 < m and copied_nums1[p1] <= nums2[p2]):
                nums1[p] = copied_nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
# Runtime: 70 ms, faster than 10.18% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 99.78% of Python3 online submissions for Merge Sorted Array.
