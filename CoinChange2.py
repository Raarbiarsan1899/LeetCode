class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        for idx, coin in enumerate(coins):
            
            if idx == 0:
                prev_array = [1 if k%coin == 0 else 0 for k in range(amount + 1)]
                
            else:
                curr_array = [1]
                for k in range(1, amount + 1):
                    if k >= coin:
                        curr_array.append(prev_array[k] + curr_array[k - coin])
                    else:
                        curr_array.append(prev_array[k])
                        
                prev_array = curr_array
                
        return prev_array[-1]
    
                
        
