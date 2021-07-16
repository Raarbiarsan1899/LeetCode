class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        list_len = len(nums)
        
        if list_len == 1:
            return 0
        
        left_sum = 0
        right_and_pivot_sum = 0
        for i in nums:
            right_and_pivot_sum += i
        
        for j in range(list_len):

            if left_sum == right_and_pivot_sum - nums[j]:
                return j

            left_sum += nums[j]
            right_and_pivot_sum -= nums[j]
            
        return -1
                
            
            
            
        
