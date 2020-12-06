""" 
エラトステネスのふるい
基本的な流れとしては、
①2からnまでの整数を全て列挙。
②列挙した値の中から最も小さな値をPとし、Pの倍数を列挙した値から削除。
③Pが√nを超えたら終了。
例： n = 10の場合。√10は3.1622.....の為、2と3の倍数を削除すれば良い。
  →[2,3,4,5,6,7,8,9,10]
  P = 2とし、リストから4,6,8,10を削除。リストには[2,3,5,7,9]が残る。
  P = 3とし、リストから9を削除。リストには[2,3,5,7]が残る。
  P = ４は√10を超える為リストに残っている数字、素数は[2,3,5,7]となる。
"""

class Solution:
    def countPrimes(self, n: int) -> int:
      # nが2以下の場合は必ず0を返す為の処理
        if n < 3:
            return 0
      # nの長さ分のリストを生成
        dp = [True] * n
      # インデックスが0と1は必ずFalseになる為、最初に処理
        dp[0] = dp[1] = False
      # 2以降の値を操作する為にfor文を回す
        for i in range(2,n):
      # 仮にdp[i]が存在する場合は処理を継続 
            if dp[i]:
      # スライスで(始点/終点/何個飛ばしで走査するかを指定)
                for j in range(i+i,n,i):
                    dp[j] = False
      # sum関数でTrueの数のみを返す
        return sum(dp)
        
# Runtime: 724 ms, faster than 45.93% of Python3 online submissions for Count Primes.
# Memory Usage: 25.6 MB, less than 54.46% of Python3 online submissions for Count Primes.
