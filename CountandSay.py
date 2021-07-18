class Solution:
    def countAndSay(self, n: int) -> str:
        
    # time complexity: O(2^N)
    # space complexity: O(2^N)
    
        if n == 1:
            return '1'
        
        prev_char = ''
        output = ''
        ct = ''
        for k in self.countAndSay(n-1):
            
            if k != prev_char:
                output = output + str(ct) + prev_char
                
                prev_char = k
                ct = 1
            else:
                ct += 1
                
        output = output + str(ct) + prev_char

        return output
