class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        for i in range(l//2 + l%2):
            for j in range(l//2):
                tmp = matrix[l-1-j][i]
                matrix[l-1-j][i] = matrix[l-1-i][l-j-1]
                matrix[l-1-i][l-j-1] = matrix[j][l-1-i]
                matrix[j][l-1-i] = matrix[i][j]
                matrix[i][j] = tmp
                
# Runtime: 32 ms, faster than 83.62% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.4 MB, less than 31.70% of Python3 online submissions for Rotate Image.

                
                
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

"""
|-|-|-|
|1|2|3|
|4|5|6|
|7|8|9|
|-|-|-|

↓

|-|-|-|
|7|4|1|
|8|5|2|
|9|6|3|
|-|-|-|
"""
