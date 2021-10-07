class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        output = []
        
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                output = [nums[left] ** 2] + output
                left += 1
            else:
                output = [nums[right] ** 2] + output
                right -= 1
                
        return output
        
        
