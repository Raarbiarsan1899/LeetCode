class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        direction = 1
        result = [''] * numRows
        
        if numRows == 1:
            return s
        
        result[0] += s[0]
        
        j = 1
        for char in s[1:]:
            
            if j == numRows - 1 or j == 0:
                direction *= -1
            
            result[j] += char 
            j += direction
            
        return ''.join(result)
            
            
        
