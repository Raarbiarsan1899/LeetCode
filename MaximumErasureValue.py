class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        max_score = 0
        seen_dict = {}
        start = 0
        subtotal = 0
        for i, k in enumerate(nums):
            if k in seen_dict and seen_dict[k] >= start:
                for j in range(start, seen_dict[k] + 1):
                    subtotal -= nums[j]
                start = seen_dict[k] + 1
            seen_dict[k] = i
            subtotal += k
            if subtotal > max_score:
                max_score = subtotal
        return max_score
                
