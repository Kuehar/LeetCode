# Plain Solution/ Time complexity O(N)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = tmp = 0
        for g in gain:
            tmp += g
            if ans < tmp:
                ans = tmp
        return ans
