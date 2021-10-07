class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        start = 0
        end = n - 1
        mid = (end + start) // 2
        
        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            mid = (end + start) // 2
            
        return start
