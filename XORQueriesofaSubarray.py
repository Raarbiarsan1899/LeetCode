class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        
        cum = [arr[0]]
        
        if len(arr) > 1:
            for i in arr[1:]:
                cum.append(cum[-1]^i)
            
        ans = []
        for j in queries:
            if j[0] == j[1]:
                ans.append(arr[j[0]])
            elif j[0] == 0:
                ans.append(cum[j[1]])
            else:
                ans.append(cum[j[0] - 1]^cum[j[1]])
                
        return ans
