class Solution:
    def numTilings(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ans_list = [0] * (n + 1)
        ans_list[0] = 1
        ans_list[1] = 1
        ans_list[2] = 2
        
        # ans_list[3] = 2*ans_list[3-3] + ans_list[3-1] + ans_list(3-2)
        
        for i in range(3, n + 1):
            ans_list[i] = ans_list[i - 1] + ans_list[i - 2]
            for j in range(i - 2):
                ans_list[i] += 2*ans_list[j]
            
            
        return ans_list[n] % 1000000007
