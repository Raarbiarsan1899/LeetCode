class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        output_table = []
        output_table.append(0)
        output_table.append(books[0][1])

        N = len(books)
        for k in range(1, N):
            
            sub_max = 0
            sub_width = 0
            candidate = []
            
            for j in range(k, -1, -1):
                sub_width += books[j][0]
            
                if sub_width > shelf_width:
                    break
                
                if books[j][1] > sub_max:
                    sub_max = books[j][1]
                
                candidate.append(output_table[j] + sub_max)
            
            output_table.append(min(candidate))
            
        return output_table[N]
