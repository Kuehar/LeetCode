class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r,_maxs = 0,len(height) - 1,0
        while l < r:
        	_maxs = max((r - l) * min(height[l],height[r]),_maxs)
        	if height[l] < height[r]:
        		l += 1
        	else:
        		r -= 1
        return _maxs
# Runtime: 1627 ms, faster than 5.02% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.4 MB, less than 89.47% of Python3 online submissions for Container With Most Water.
