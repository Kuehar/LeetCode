class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop(-1))
# Runtime: 3056 ms, faster than 16.74% of Python3 online submissions for Rotate Array. O(N)
# Memory Usage: 25.3 MB, less than 96.76% of Python3 online submissions for Rotate Array.
        
