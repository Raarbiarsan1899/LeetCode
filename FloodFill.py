class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                
                if r >= 1:
                    dfs(r - 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if r < len(image) - 1:
                    dfs(r + 1, c)
                if c < len(image[0]) - 1:
                    dfs(r, c + 1)
                
        dfs(sr, sc)
        
        return image
