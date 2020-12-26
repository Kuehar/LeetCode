class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_1,nums_2 = sorted(nums1),sorted(nums2)
        pointer1 = pointer2 = 0
        ans = []
        while True:
            try:
                if nums_1[pointer1] > nums_2[pointer2]:
                    pointer2 += 1
                elif nums_1[pointer1] < nums_2[pointer2]:
                    pointer1 += 1
                else:
                    ans.append(nums_1[pointer1])
                    pointer1 += 1
                    pointer2 += 1
            except IndexError:
                break
        return ans
# Runtime: 32 ms, faster than 99.79% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.4 MB, less than 50.81% of Python3 online submissions for Intersection of Two Arrays II.
