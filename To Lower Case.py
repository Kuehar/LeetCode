class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
# Runtime: 24 ms, faster than 91.12% of Python3 online submissions for To Lower Case.
# Memory Usage: 14 MB, less than 15.17% of Python3 online submissions for To Lower Case.


class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ''
        for s in str:
            if ord(s) >=  ord('A') and ord(s) <= ord('Z'):
                ans +=chr(ord(s) - (ord('A') - ord('a')))
            else:
                ans += s
        return ans
            
        
