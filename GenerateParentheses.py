class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []
        
        if n == 0:
            return ['']
        # if n == 1:
        #     return ['()']
        
        for k in range(n):
            # if 2*k >= n:
                a = self.generateParenthesis(k)
                b = self.generateParenthesis(n-k-1)

                for i in a:
                    for j in b:
                        results.append('({}){}'.format(i, j))
                        
        return results
