class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for row_num in range(numRows):
            # The first and last elements in each row are always 1
            row = [1] * (row_num + 1)
            
            # Each inner element is the sum of the two elements directly above it
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
                
            triangle.append(row)
            
        return triangle
