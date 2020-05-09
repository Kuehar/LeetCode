class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank,start,cur = 0,0,0
        for i in range(len(gas)):
            cur += (gas[i] - cost[i])
            tank += (gas[i] - cost[i])
            if cur < 0:
                cur = 0
                start = i + 1
        if tank < 0:
            return -1
        else:
            return start
# Runtime: 56 ms, faster than 53.48% of Python3 online submissions for Gas Station.
# Memory Usage: 14.6 MB, less than 6.25% of Python3 online submissions for Gas Station.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank,start,cur = 0,0,0
        for i in range(len(gas)):
            cur += (gas[i] - cost[i])
            tank += (gas[i] - cost[i])
            if cur < 0:
                cur = 0
                start = i + 1
        return -1 if tank < 0 else start
# Runtime: 52 ms, faster than 76.94% of Python3 online submissions for Gas Station.
# Memory Usage: 14.9 MB, less than 6.25% of Python3 online submissions for Gas Station.