class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
#         if len(t) == 0 or len(s) == 0:
#             return 0
        
#         if s == t:
#             return 1

#         output = 0
#         if len(t) == 1:
#             for i in range(len(s)):
#                 if s[i] == t:
#                     output += 1
#         else:
#             for i in range(len(s)):
#                 if s[i] == t[-1]:
#                     output += self.numDistinct(s[:i], t[:-1])
            
#         return output
        
        if len(s) < len(t):
            return 0
    
        if t[0] == s[0]:
            output_dict = {(0, 0):1}
        else:
            output_dict = {(0, 0):0}
        for i in range(len(t)):
            for j in range(i, len(s)):
                if i == 0:
                    if j != 0:
                        if t[i] == s[j]:
                            output_dict[(i, j)] = output_dict[(i, j-1)] + 1
                        else:
                            output_dict[(i, j)] = output_dict[(i, j-1)]
                else:
                    if i == j:
                        if t[i] == s[j]:
                            output_dict[(i, j)] = output_dict[(i-1, j-1)]
                        else:
                            output_dict[(i, j)] = 0
                    else:
                        if t[i] == s[j]:
                            output_dict[(i, j)] = output_dict[(i-1, j-1)] + output_dict[(i, j-1)]
                        else:
                            output_dict[(i, j)] = output_dict[(i, j-1)]
                            
        return output_dict[(len(t)-1, len(s)-1)]
