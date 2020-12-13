# 常に最善の手を選び続けるという内容のバックトラック法。あまり実装をしたことがなかったので非常に時間がかかった。
# 計算量はO(N^2)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 探索範囲の走査
        for i in range(len(board)):
            for j in range(len(board[i])):
                # backtrack関数呼び出し
                if self.backtrack(i,j,board,word):
                    return True
        return False
    
    # backtrack(判定)アルゴリズム
    def backtrack(self,i,j,board,word):
        if len(word) == 0:
                return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        # もしwordの最初の文字とboardの該当文字が合致すればbacktrack処理を始める
        if board[i][j] == word[0]:
            # 同じ文字は一回しか使えない為無効化する
            board[i][j] = "-"
            # 縦横のいずれかの値が合致すれば処理を続ける
            if self.backtrack(i+1,j,board,word[1:]) or self.backtrack(i-1,j,board,word[1:]) or self.backtrack(i,j+1,board,word[1:]) or self.backtrack(i,j-1,board,word[1:]):
                return True
            board[i][j] = word[0]
        return False
# Runtime: 364 ms, faster than 49.96% of Python3 online submissions for Word Search.
# Memory Usage: 15.5 MB, less than 56.91% of Python3 online submissions for Word Search.
