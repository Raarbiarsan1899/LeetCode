class Solution:
    def minimumBoxes(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        i = 2
        F = 1
        next_F = 4
        while True:
            if n > F and n <= next_F:
                break
            F = next_F
            i += 1
            next_F = i*(i+1)*(2*i+1)/12 + i*(i+1)/4
        
        j = 1
        f = 0
        next_f = 1
        while True:
            if n - F > f and n - F <= next_f:
                break
            f = next_f
            j += 1
            next_f = j*(j+1)/2
        
        return int((i-1)*i/2 + j)
