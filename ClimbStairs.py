class Solution:
    def climbStairs(self, n: int) -> int:
        
        table = [1, 2]
        
        for i in range(2, n):
            table.append(table[i-1] + table[i-2])
        
        return table[n-1]
