class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m_idx = m - 1
        n_idx = n - 1
        fill_idx = m + n - 1
        
        while m_idx >= 0 and n_idx >= 0:

            if nums1[m_idx] > nums2[n_idx] or n_idx < 0:
                nums1[fill_idx] = nums1[m_idx]
                m_idx -= 1
            elif nums1[m_idx] <= nums2[n_idx] or m_idx < 0:
                nums1[fill_idx] = nums2[n_idx]
                n_idx -= 1
            fill_idx -= 1
              
        while n_idx >= 0:
            nums1[fill_idx] = nums2[n_idx]
            n_idx -= 1
            fill_idx -= 1
            
            
            
        
