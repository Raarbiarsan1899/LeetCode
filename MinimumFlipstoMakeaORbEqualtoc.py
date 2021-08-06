class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a != 0 or b != 0 or c != 0:
            
            remain_a = a % 2
            remain_b = b % 2
            remain_c = c % 2
            
            if remain_c == 0:
                if remain_a == 1:
                    ans += 1
                if remain_b == 1:
                    ans += 1
                    
            else:
                if remain_a == 0 and remain_b == 0:
                    ans += 1
                    
            a = a >> 1
            b = b >> 1
            c = c >> 1
                    
        return ans
                    
        
