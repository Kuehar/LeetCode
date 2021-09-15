class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # それぞれのインデックスの値をlen()で取った値と比較してオーバーしたらFalse,==になったらTrueでいい気がする・・・・
        # 最大ジャンプ長(3なら1,2でも可能)なのでダメでした。やはりDP...
        length = len(nums)
        ind = 0
        while length > ind:
            if nums[ind] == nums[-1]:
                return True
            elif nums[ind] == 0:
                return False
            print(ind)
            ind += nums[ind]
        return False
