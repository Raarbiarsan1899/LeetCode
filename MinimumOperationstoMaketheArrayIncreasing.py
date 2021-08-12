class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = 0
        prev_num = nums[0]
        
        for num in nums[1:]:
            if num <= prev_num:
                ans += prev_num - num + 1
                prev_num += 1
            else:
                prev_num = num
                
        return ans
                
        
