class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        if left == right:
            return left
        
        k = 1
        while k <= right - left:
            if k >= left:
                return 0
            k = k*2
        
        left_new = left // k
        right_new = right // k
        
        return k*self.rangeBitwiseAnd(left_new, right_new)
