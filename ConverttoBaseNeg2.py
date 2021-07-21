class Solution:
    def baseNeg2(self, n: int) -> str:
        
        digit = ''
        
        if n == 0:
            return "0"
        
        k = n
        
        while k != 0:
            
            if k > 0:
                remain = k%2
            else:
                remain = (-k)%2
                
            digit = str(remain) + digit
            k = int((k-remain)/-2)
            
        return digit
