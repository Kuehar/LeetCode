class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
            dic[arr[i]] += 1
            if dic[arr[i]] >= k:
                return arr[i]
        return arr[-1]
# Runtime: 760 ms, faster than  62.35%  of  Python3  online submissions for  Find the Winner of an Array Game.

# Memory Usage: 27.7 MB, less than  24.52%  of  Python3  online submissions for  Find the Winner of an Array Game.
