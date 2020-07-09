import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        key = count.get
        return heapq.nlargest(k,count.keys(),key)
# Runtime: 108 ms, faster than 66.40% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.2 MB, less than 79.07% of Python3 online submissions for Top K Frequent Elements.
なお、nlargestの引数はn, iterable, key=Noneという順番です。

では今回はここまで。
お疲れ様でした。


ストック
0
KueharX
くえはる
@KueharX
ブログ始めました。
https://kueharx.blogspot.com/
概要
問題
解
