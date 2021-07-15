class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        class Node:
            
            def __init__(self, value, depth):
                self.value = value
                self.depth = depth
                # self.child = []
                self.parent = None
        
        list_length = len(nums)

        leaves = {}
        node_dict = {}
        
        deepest = 0
        
        for i in range(list_length):
            position = list_length - 1 - i
            
            node_dict[position] = Node(nums[position], 1)
            _curr_value = nums[position]
            
            max_depth = 0
            max_parent = None
            
            for j, k in leaves.items():

                p = j
                while node_dict[p].value <= _curr_value and node_dict[p].parent is not None:
                    p = node_dict[p].parent
                if node_dict[p].value > _curr_value:
                    curr_depth = node_dict[p].depth
                    if curr_depth > max_depth:
                        max_depth = curr_depth
                        max_parent = p
            
            if max_parent is not None:
                node_dict[position].parent = max_parent
                node_dict[position].depth = max_depth + 1
                # node_dict[max_parent].child.append(position)
                
                if max_parent in leaves.keys():
                    del leaves[max_parent]
                
            if max_depth + 1 > deepest:
                deepest = max_depth + 1
            leaves[position] = node_dict[position]
            
            # print([(_key, _value.value, _value.depth) for _key, _value in leaves.items()])
            # print([(_key, _value.value, _value.depth) for _key, _value in node_dict.items()])

            
        return deepest
