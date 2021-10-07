class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        output = []
        length = len(nums)
        
        pos_idx = -1
        for idx, num in enumerate(nums):
            if num >= 0:
                pos_idx = idx
                break
        
        if pos_idx == -1: # all negative
            for i in range(length):
                output.append(nums[length - i - 1] ** 2)
            return output        
        elif pos_idx == 0:
            for i in range(length):
                output.append(nums[i] ** 2)
            return output
        
        neg_idx = pos_idx - 1
        while neg_idx >= 0 or pos_idx <= length - 1:

            if pos_idx > length - 1:
                output.append(nums[neg_idx] ** 2)
                neg_idx -= 1
            elif neg_idx < 0:
                output.append(nums[pos_idx] ** 2)
                pos_idx += 1
            else:
                if nums[pos_idx] ** 2 > nums[neg_idx] ** 2:
                    output.append(nums[neg_idx] ** 2)
                    neg_idx -= 1
                else:
                    output.append(nums[pos_idx] ** 2)
                    pos_idx += 1
                    
        return output
        
        
