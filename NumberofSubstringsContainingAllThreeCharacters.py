class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        window = ''
        ct = {'a':0, 'b':0, 'c':0}
        ans = 0
        window_left = 0
        
        for idx, char in enumerate(s):
            
            window += char
            ct[char] += 1

            if ct['a'] == 0 or ct['b'] == 0 or ct['c'] == 0:
                pass
                
            else:
                while ct[window[0]] - 1 != 0:
                    ct[window[0]] -= 1
                    window = window[1:]
                    window_left += 1
                ans += window_left + 1
                
        return ans
