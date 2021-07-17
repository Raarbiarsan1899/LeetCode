class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        total_piles = len(piles)
        
        score_table = {}
        
        for i in range(total_piles):
            
            if i == 0:
                for j in range(0, total_piles - i):
                    score_table[(j, j)] = 0 # piles[j]
            else:
                for j in range(0, total_piles - i):
                    
                    if (j-i-total_piles) % 2 == 1:
                        if score_table[(j+1, j+i)] + piles[j] > score_table[(j, j+i-1)] + piles[j+1]:
                            score_table[(j, j+i)] = score_table[(j+1, j+i)] + piles[j]
                        else:
                            score_table[(j, j+i)] = score_table[(j, j+i-1)] + piles[j+1]
                    else:
                        if score_table[(j+1, j+i)] - piles[j] < score_table[(j, j+i-1)] - piles[j+1]:
                            score_table[(j, j+i)] = score_table[(j+1, j+i)] - piles[j]
                        else:
                            score_table[(j, j+i)] = score_table[(j, j+i-1)] - piles[j+1]
                            
                            
        return score_table[(0, total_piles-1)] > 0
