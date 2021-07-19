class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            min_string = s
            for i in range(len(s)):
                if s[i:] + s[:i] < min_string:
                    min_string = s[i:] + s[:i]
            return min_string
        else:
            return ''.join(sorted(s))
