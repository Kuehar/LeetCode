class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

# Runtime: 36 ms, faster than 36.25% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [0]*len(index)
        j = 0
        while j < len(index):
            target.insert(index[j], nums[j])
            j += 1
        return target[:len(nums)]

# Runtime: 36 ms, faster than 36.25% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.
...あれ？
同じやんけ。
むしろメモリの使用量ちょっと少ないし。

ま、まぁ一旦ひとまずこれはおいておいて、大幅に速度が上がるものではありませんでした。

私が思いつかなかったものとしては、zip関数を使ったもの、スライスを使ったものです。

zip関数は、公式ドキュメントに記載されている通り、

それぞれのイテラブルから要素を集めたイテレータを作ります。
この関数はタプルのイテレータを返し、その i 番目のタプルは引数シーケンスまたはイテラブルそれぞれの i 番目の要素を含みます。このイテレータは、入力イテラブルの中で最短のものが尽きたときに止まります。単一のイテラブル引数が与えられたときは、1 要素のタプルからなるイテレータを返します。引数がなければ、空のイテレータを返します。

というもので、

hoge = [1,2,3,4,5]
foo = [6,7,8,9,10]
bar = zip(hoge,foo)
list(bar)
[(1,6),(2,7),(3,8),(4,9),(5,10)]
以上のような動きをします。

なお、これを使っているものとしては、こちら。

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, v in zip(index, nums):
            res.insert(i, v)
        return res
# Runtime: 28 ms, faster than 90.08% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.