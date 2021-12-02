class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()
# Runtime: 208 ms, faster than 82.72% of Python3 online submissions for Reverse String.
# Memory Usage: 18.3 MB, less than 5.81% of Python3 online submissions for Reverse String.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return ''.join(reversed(list(s)))
    
   
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # space complexity O(n)
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left+1,right-1)
                
                
        return helper(0,len(s)-1)
# Runtime: 220 ms, faster than 30.35% of Python3 online submissions for Reverse String.
# Memory Usage: 45.7 MB, less than 5.30% of Python3 online submissions for Reverse String.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # space complexity O(n)
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0,len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1
# Runtime: 204 ms, faster than 54.14% of Python3 online submissions for Reverse String.
# Memory Usage: 18.7 MB, less than 18.49% of Python3 online submissions for Reverse String.
