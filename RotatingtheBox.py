class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        ans = [""] * len(box[0])
        
        for row in box:
            
            stack = 0
            start = 0
            new_row = []
            for place, status in enumerate(row):

                if status == "#":
                    stack += 1
                
                if status == "*":
                    new_row += ["."] * (place - start - stack) + ["#"] * stack + ["*"]
                    stack = 0
                    start = place + 1
                    
                elif place == len(row) - 1:
                    new_row += ["."] * (place - start + 1 - stack) + ["#"] * stack
                    stack = 0
            
            for j,k in enumerate(new_row):
                ans[j] = k + ans[j]
                
        return ans
            
