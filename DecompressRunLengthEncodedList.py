class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        list_len = len(nums) // 2
        a = []
        for k in range(list_len):
            
            a = a + [nums[2*k+1]]*nums[2*k]
        return a
