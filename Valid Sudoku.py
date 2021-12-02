class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # 行、列、3*3の正方形に1~9までの数字が1度ずつだけ出れば正しい事になるのでそれぞれの単位をset()を使って管理する
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # それぞれの値を各項目でチェックする
                if val == ".":
                    continue
                
                # 列チェック
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 行チェック
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3*3の正方形チェック
                index = (r//3)*3+c//3
                if val in boxes[index]:
                    return False
                boxes[index].add(val)
                
        return True
# Runtime: 92 ms, faster than 89.55% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 14.4 MB, less than 43.74% of Python3 online submissions for Valid Sudoku.
