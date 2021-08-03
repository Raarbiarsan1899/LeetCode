class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        type_xy = 0
        type_yx = 0
        
        for i in range(len(s1)):
            
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x':
                type_xy += 1
            elif s1[i] == 'y':
                type_yx += 1
        
        if (type_xy + type_yx) % 2 != 0:
            return -1
        elif type_xy % 2 == 0:
            return type_xy//2 + type_yx//2
        else:
            return type_xy//2 + type_yx//2 + 2
            
