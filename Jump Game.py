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
    
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # それぞれのインデックスの値をlen()で取った値と比較してオーバーしたらFalse,len=<になったらTrueでいい気がする・・・・
        # 追記：前提を間違えていて、そもそもdp>len-1で辿り着けるかを求めるだけでよかった・・・・
        length = len(nums)
        ind = 0
        dp = [0]*length
        dp[0] = nums[0]
        for i in range(1,length-1):
            # もしiがDP[i-1]の値を上回った場合(dp[1]から後が0だった場合)にはFalse
            if dp[i-1] < i:
                return False
            dp[i] = max(i+nums[i],dp[i-1])
            
            if dp[i] >= length-1:
                return True
        return dp[length-2] >= length-1
# Runtime: 495 ms, faster than 63.61% of Python3 online submissions for Jump Game.
# Memory Usage: 15.3 MB, less than 70.47% of Python3 online submissions for Jump Game.
