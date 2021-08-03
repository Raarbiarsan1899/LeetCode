# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        
        def dfs(node, leaf_list):
            
            if node.left is None and node.right is None:
                leaf_list.append(node.val)
                
            if node.left is not None:
                dfs(node.left, leaf_list)
                
            if node.right is not None:
                dfs(node.right, leaf_list)
                
        leaf_list1 = []
        dfs(root1, leaf_list1)
        
        leaf_list2 = []
        dfs(root2, leaf_list2)
        
        return leaf_list1 == leaf_list2
        
