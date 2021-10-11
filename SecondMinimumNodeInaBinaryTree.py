# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
#     def getMinimalTwo(self, node):

#         if node.left is None:
#             return [node.val]

#         else:
#             a = set(self.getMinimalTwo(node.left) + self.getMinimalTwo(node.right))
#             return sorted(list(a))[:2]
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        def getMinimalTwo(node):

            if node.left is None:
                return [node.val]

            else:
                a = set(getMinimalTwo(node.left) + getMinimalTwo(node.right))
                return sorted(list(a))[:2]
        
        # ans = self.getMinimalTwo(root)
        ans = getMinimalTwo(root)
        if len(ans) > 1:
            return ans[1]
        else:
            return -1
        
        
        
