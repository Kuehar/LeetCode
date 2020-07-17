class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_num = max_num = 0
        min_num = max(weights)
        max_num = sum(weights)

        while min_num < max_num:
            mid = (min_num + max_num)//2
            days = temp_weight = 0
            for i in weights:
                temp_weight += i
                if temp_weight > mid:
                    days += 1
                    temp_weight = i
            if days + 1 <= D:
                max_num = mid
            else:
                min_num = mid+1

        return min_num
# Runtime: 508 ms, faster than 92.24% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 17.1 MB, less than 7.21% of Python3 online submissions for Capacity To Ship Packages Within D Days.
