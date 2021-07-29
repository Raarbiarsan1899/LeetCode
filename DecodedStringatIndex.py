class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        string = ['']
        string_len = [0]
        prev_char = s[0]
        for char in s:
            if char >= '2' and char <= '9':
                if prev_char >= 'a' and prev_char <= 'z':
                    string_len.append(string_len[-1])
                    string_len[-1] = (len(string[-1]) + string_len[-1]) * (int(char))
                elif prev_char >= '2' and prev_char <= '9':
                    string_len[-1] = string_len[-1] * (int(char))
                
            elif char >= 'a' and char <= 'z':
                if prev_char >= '2' and prev_char <= '9':
                    string.append('')
                    
                string[-1] += char
                
            prev_char = char
        
        k = k - 1
        for i in range(len(string_len) - 1, 0, -1):
            if string_len[i] > k:
                pass
            else:
                k = k % (string_len[i] + len(string[i]))
                if k >= string_len[i]:
                    return string[i][k - string_len[i]]
                
        return string[0][k % len(string[0])]
