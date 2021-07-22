# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        right = n
        left = 1
        k = n // 2
        while guess(k) != 0:
            
            if guess(k) == -1:
                right = k
                k = (k + left) // 2
                
            elif guess(k) == 1:
                left = k
                k = (k + right)//2 + 1
                
        return k
                
                
            
