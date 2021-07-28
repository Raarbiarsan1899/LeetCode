class Solution:
    def numOfWays(self, n: int) -> int:
        
        class Node:
            def __init__(self, name: str):
                self.name = name
                self.neighbor = []
                self.ways = 0
                
            def add_neighbor(self, new_neighbor):
                self.neighbor.append(new_neighbor)
        
        color = ['r', 'y', 'g']
        tricolor = []
        for i in color:
            for j in color:
                for k in color:
                    if i != j and j != k:
                        tricolor.append(i+j+k)
        
        pattern = {}
        for pattern1 in tricolor:
            pattern[pattern1] = Node(pattern1)
            for pattern2 in tricolor:
                if pattern1[0] != pattern2[0] and pattern1[1] != pattern2[1] and pattern1[2] != pattern2[2]:
                    pattern[pattern1].add_neighbor(pattern2)

        if n == 1:
            return len(tricolor)
        
        ways = {}
        for pattern1 in tricolor:
            ways[pattern1] = [1, 1]
            
        for i in range(1, n):
            for pattern1 in tricolor:
                ways[pattern1][1] = sum([ways[k][0] for k in pattern[pattern1].neighbor])
            for pattern1 in tricolor:
                ways[pattern1][0] = ways[pattern1][1]
        
        total = 0
        for pattern1 in tricolor:
            total += ways[pattern1][1]
                    
        return total % 1000000007
                
        
