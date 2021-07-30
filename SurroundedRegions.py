class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        
        def dfs(chess: Tuple[int]):
            
            explored.append(chess)
            
            if chess[0] == m - 1 or chess[0] == 0 or chess[1] == n - 1 or chess[1] == 0:
                not_surrounded = True
            else:
                not_surrounded = False
            
            if chess[0] + 1 <= m - 1:
                if (chess[0] + 1, chess[1]) not in explored and board[chess[0] + 1][chess[1]] == 'O':
                    a = dfs((chess[0] + 1, chess[1]))
                    not_surrounded = not_surrounded or a
                    
            if chess[0] - 1 >= 0:
                if (chess[0] - 1, chess[1]) not in explored and board[chess[0] - 1][chess[1]] == 'O':
                    b = dfs((chess[0] - 1, chess[1]))
                    not_surrounded = not_surrounded or b
                    
            if chess[1] - 1 >= 0:
                if (chess[0], chess[1] - 1) not in explored and board[chess[0]][chess[1] - 1] == 'O':
                    c = dfs((chess[0], chess[1] - 1))
                    not_surrounded = not_surrounded or c

            if chess[1] + 1 <= n - 1:
                if (chess[0], chess[1] + 1) not in explored and board[chess[0]][chess[1] + 1] == 'O':
                    d = dfs((chess[0], chess[1] + 1))
                    not_surrounded = not_surrounded or d
            
            return not_surrounded
            
            
        m = len(board)
        n = len(board[0])
        
        for i in [0, m-1]:
            
            for j in range(n):
                
                if board[i][j] == 'O':
                    explored = []
                    not_surr = dfs((i, j))
                    
                    if not_surr:
                        for k in explored:
                            board[k[0]][k[1]] = 'A'
                            
        for i in range(m):
            
            for j in [0, n-1]:
                
                if board[i][j] == 'O':
                    explored = []
                    not_surr = dfs((i, j))
                    
                    if not_surr:
                        for k in explored:
                            board[k[0]][k[1]] = 'A'
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        
            
            
