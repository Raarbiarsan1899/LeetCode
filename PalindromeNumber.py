class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        elif x == 0:
            return True
        
        mods = []
        while x != 0:
            mods.append(x % 10)
            x = x // 10
        
        left = 0
        right = len(mods) - 1
        
        while left <= right:
            if mods[left] == mods[right]:
                pass
            else:
                return False
            left += 1
            right -= 1
            
        return True
            
            
            
