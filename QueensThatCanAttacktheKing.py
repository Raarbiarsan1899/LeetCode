class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        
        direction = [(-1, -1, 0, 0),
                     (-1, 0, 0, 10),
                     (-1, 1, 0, 7),
                     (0, 1, 10, 7),
                     (1, 1, 7, 7),
                     (1, 0, 7, 10),
                     (1, -1, 7, 0),
                     (0, -1, 10, 0)
                    ]
        
        qs = []
        for d in direction:
            position_r = king[0]
            position_c = king[1]
            Met = False
            while not Met and position_r != d[2] and position_c != d[3]:
                position_r += d[0]
                position_c += d[1]
                if [position_r, position_c] in queens:
                    Met = True
                    qs.append([position_r, position_c])
                    
        return qs
                    
            
        
