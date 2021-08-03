# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        total = 0
        
        if not root:
            return 0
        
        def dfs(node):
            
            nonlocal total
            
            if node.left is not None:  # and node.left not in explored:
                left_sum = dfs(node.left) 
            else:
                left_sum = 0
                
            if node.right is not None:
                right_sum = dfs(node.right)
            else:
                right_sum = 0
            
            total += abs(left_sum - right_sum) 
            
            return left_sum + right_sum + node.val
            
        dfs(root)
        
        return total
