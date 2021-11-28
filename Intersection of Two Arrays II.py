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


# リストの長さが違う←pointerでwhile文の添字を使える。例外処理でIndeErrorを拾えばよし。添字ではなく値を返す場合にはsortしても可。ただし計算量が増える点には注意。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = p2 = 0
        ans = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        #  IndexErrorを起こすまで繰り返す
        while True:
            try:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                elif nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    ans.append(nums1[p1])
                    p1 += 1
                    p2 += 1
            except IndexError:
                break
        return ans
