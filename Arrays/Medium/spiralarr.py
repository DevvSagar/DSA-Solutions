class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        m = len(matrix)
        n = len(matrix[0])
        
        # Define the 4 boundaries (walls)
        s_row = 0
        e_row = m - 1
        s_col = 0
        e_col = n - 1
        
        ans = []
        
        while s_row <= e_row and s_col <= e_col:
            # 1. Move RIGHT across Top Row
            for col in range(s_col, e_col + 1):
                ans.append(matrix[s_row][col])
            s_row += 1  # Top row is collected, push top wall down
            
            # 2. Move DOWN along Right Column
            for row in range(s_row, e_row + 1):
                ans.append(matrix[row][e_col])
            e_col -= 1  # Right column is collected, push right wall left
            
            # 3. Move LEFT across Bottom Row
            # (Check needed so we don't re-print a row if walls already crossed)
            if s_row <= e_row:
                for col in range(e_col, s_col - 1, -1):
                    ans.append(matrix[e_row][col])
                e_row -= 1  # Bottom row is collected, push bottom wall up
                
            # 4. Move UP along Left Column
            # (Check needed so we don't re-print a column if walls already crossed)
            if s_col <= e_col:
                for row in range(e_row, s_row - 1, -1):
                    ans.append(matrix[row][s_col])
                s_col += 1  # Left column is collected, push left wall right
                
        return ans