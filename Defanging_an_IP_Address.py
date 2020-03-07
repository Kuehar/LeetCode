"""
https://leetcode.com/problems/defanging-an-ip-address/submissions/
"""


"""
   Runtime:28ms
   Memory:12.8MB
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.','[.]')
        return address
