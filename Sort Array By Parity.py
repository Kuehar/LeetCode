class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # lambda式で引数として与えられたxの値を2で割って余りが0のものをソートして前に持ってくる
        nums.sort(key = lambda x: x%2)
        return nums
