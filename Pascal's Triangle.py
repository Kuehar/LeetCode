class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        triangle = [[1]]
        
        for i in range(1,numRows):
            row = [1]
              
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            
            row.append(1)
            triangle.append(row)
            
        return triangle
# Runtime: 28 ms, faster than 73.84% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.
                
