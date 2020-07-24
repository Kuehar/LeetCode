class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1,set2 = set(nums1),set(nums2)
        return list(set1&set2)
# Runtime: 56 ms, faster than 44.78% of Python3 online submissions for Intersection of Two Arrays.
