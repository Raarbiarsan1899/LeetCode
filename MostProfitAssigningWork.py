class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        n = len(difficulty)
        m = len(worker)
        
        s_idx = sorted(range(n), key = lambda k: difficulty[k])
        
        max_profit = {difficulty[s_idx[0]]:profit[s_idx[0]]}
        prev_diff = difficulty[s_idx[0]]
        prev_profit = profit[s_idx[0]]
        
        for k in range(1, n):
            if profit[s_idx[k]] > max_profit[difficulty[s_idx[k - 1]]]:
                max_profit[difficulty[s_idx[k]]] = profit[s_idx[k]]
            else:
                max_profit[difficulty[s_idx[k]]] = max_profit[difficulty[s_idx[k - 1]]]

        output = 0
        j = 0
        
        for i in sorted(worker):
            while j < n and i >= difficulty[s_idx[j]]:
                j += 1
            if j > 0:
                output += max_profit[difficulty[s_idx[j-1]]]
            
        return output
