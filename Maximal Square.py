class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        square_size = 0
        dp = [[0]*(col+1) for i in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if (matrix[i-1][j-1] == '1'):
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    square_size = max(square_size,dp[i][j])
        return square_size**2
# Runtime: 200 ms, faster than 86.93% of Python3 online submissions for Maximal Square.
# Memory Usage: 15.7 MB, less than 53.98% of Python3 online submissions for Maximal Square.
