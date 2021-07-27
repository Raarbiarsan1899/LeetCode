class Solution:
    def minSwaps(self, s: str) -> int:
        
        ct_0 = 0
        ct_1 = 0
        
        pos = 0
        odd_0 = 0
        odd_1 = 0
        even_0 = 0
        even_1 = 0
        
        for char in s:
            if char == '0':
                ct_0 += 1
                if pos % 2 == 0:
                    odd_0 += 1
                else:
                    even_0 += 1
                
            elif char == '1':
                ct_1 += 1
                if pos % 2 == 0:
                    odd_1 += 1
                else:
                    even_1 += 1
            pos += 1

        if ct_0 - ct_1 < -1 or ct_0 - ct_1 > 1:
            return -1
        
        if ct_0 == ct_1:
            return min(odd_1, even_1)
        
        if ct_0 - ct_1 == 1:
            return even_0
        if ct_1 - ct_0 == 1:
            return even_1
