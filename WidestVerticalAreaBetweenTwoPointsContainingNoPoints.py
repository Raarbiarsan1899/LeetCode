class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        width_list = sorted([p[0] for p in points])
        
        max_width = 0
        prev_width = width_list[0]
        for k in range(1, len(width_list)):
            if width_list[k] - prev_width > max_width:
                max_width = width_list[k] - prev_width
            prev_width = width_list[k]
                
        return max_width
