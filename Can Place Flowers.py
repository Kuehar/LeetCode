class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if len(flowerbed) == 0: return False
        if len(flowerbed) == 1: return flowerbed[0] == 0
            
        pre,cur = flowerbed[0],flowerbed[1]
        if pre + cur == 0:
            flowerbed[0] = 1
            n -= 1
            
        cur,nex = flowerbed[-1],flowerbed[-2]
        if cur + nex == 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(2,len(flowerbed)-2):
            pre = flowerbed[i-1]
            cur = flowerbed[i]
            nex = flowerbed[i+1]
            if (pre + cur + nex) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
# Runtime: 164 ms, faster than 58.48% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.5 MB, less than 89.00% of Python3 online submissions for Can Place Flowers.
