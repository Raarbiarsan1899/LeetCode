class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if sum(nums) == 0:
            return '0'
        
        def compare(a, b):
            
            min_len = min(len(a), len(b))
            
            k = 0
            while k < min_len:
            
                if int(a[k]) > int(b[k]):
                    return True
                elif int(a[k]) < int(b[k]):
                    return False
                k += 1
            
            if len(a) < len(b):
                return compare(a, b[min_len:])
            elif len(a) > len(b):
                return compare(a[min_len:], b)
            else:
                return True
                
        ordered_list = []
        
        for i in nums:
            insertion_pos = None
            for idx, j in enumerate(ordered_list):
                if compare(str(i), str(j)):
                    insertion_pos = idx
                    break
            if insertion_pos is not None:
                ordered_list.insert(insertion_pos, str(i))
            else:
                ordered_list.append(str(i))
        
        
        return ''.join(ordered_list)
