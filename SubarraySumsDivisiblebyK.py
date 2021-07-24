class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        store = [0] * k
        store[0] = 1
        output = 0
        total = 0
        
        for i in nums:
            total += i
            output += store[total%k]
            store[total%k] = store[total%k] + 1
            
        return output
        
