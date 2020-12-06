"""
At first,row,searching for column and low whether the path is unique.
and 
"""


"""
Test Case
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 仮にスタート地点が1だった場合は道が存在しないため、初期条件としてobstacleGrid[0][0] == 1だった場合は無条件で0を返す
        if obstacleGrid[0][0] == 1:
            return 0
        
        #  DPの初期化
        obstacleGrid[0][0] = 1
        
        # 横と縦の長さをそれぞれ取得
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # mの長さ分走査していき、それぞれの値が1の時のみ障害物がない値の1を格納する
        for i in range(1,m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1-obstacleGrid[i][0])
        
        # nの長さ分走査していき、それぞれの値が1の時のみ障害物がない値の1を格納する
        for j in range(1,n):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1-obstacleGrid[0][j])
            
        # 二重for文,O(n^2)でそれぞれの要素を全て走査していく。
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j] = (1-obstacleGrid[i][j])*(obstacleGrid[i-1][j]+obstacleGrid[i][j-1])

        # 最終的な値を返す為にスライスで一番後ろの値を指定する
        return obstacleGrid[-1][-1]
# Runtime: 36 ms, faster than 92.19% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.2 MB, less than 37.22% of Python3 online submissions for Unique Paths II.
