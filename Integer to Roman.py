class Solution:
    def intToRoman(self, num: int) -> str:
        nums = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
        roman = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
        ans = ""
        while num != 0:
            for i, j in enumerate(nums):
                if num >= j:
                    num -= j
                    ans += roman[i]
                    break
        return ans
# Runtime: 52 ms, faster than 60.03% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.9 MB, less than 33.48% of Python3 online submissions for Integer to Roman.
