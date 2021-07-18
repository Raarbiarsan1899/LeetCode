# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

# Space complexity: O(V)
# Time complexity: O(V+E)
        
        node_list = [root]
        index_list = [''] # [0]
        
        while len(index_list) != 0:

            leftmost_index = index_list[0]
            rightmost_index = index_list[-1]
            
            N = len(index_list)
            for i in range(N):
                
                tmp_node = node_list.pop(0)
                tmp_index = index_list.pop(0)

                if tmp_node.left is not None:
                    node_list.append(tmp_node.left)
                    index_list.append(tmp_index + '0')   # (tmp_index*2)
                if tmp_node.right is not None:
                    node_list.append(tmp_node.right)
                    index_list.append(tmp_index + '1')  # (tmp_index*2+1)
                    
            layer += 1

        str_len = len(leftmost_index)

        output_node = root
        for k in range(str_len):
            
            left_char = leftmost_index[k]
            right_char = rightmost_index[k]
            
            if left_char == right_char:
                            
                if left_char == '0' and output_node.left is not None:
                    output_node = output_node.left
                elif left_char == '1' and output_node.right is not None:
                    output_node = output_node.right
            else:
                break
                
        return output_node
            
