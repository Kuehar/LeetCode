class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:         
        # DFS
        island_sum = 0
        # 2次元配列の縦と横の長さ分ループ
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    island_sum += 1
        return island_sum
    
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = "/"
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        # gridの縦と横の数を取得する
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q = collections.deque([(i,j)])
                    grid[i][j] = "-"
                    while q:
                        x,y = q.popleft()
                        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                            xx,yy = x+dx,y+dy
                            if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] == '1':
                                q.append((xx, yy))
                                grid[xx][yy] = '2'
                    ans += 1
        return ans
