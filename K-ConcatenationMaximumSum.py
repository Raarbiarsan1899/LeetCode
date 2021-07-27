class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def kadane(subarray):
            max_contig = 0
            current_contig = 0
            for i in subarray:
                current_contig = max(current_contig + i, 0)
                if current_contig > max_contig:
                    max_contig = current_contig
            return max_contig
        
        # mono = kadane(arr)
        # di = kadane(arr*2)
        # if k == 1:
        #     return mono
        # else:
        #     return max(di, sum(arr)*(k-2) + di) % (10**9+7)
        
        return kadane(arr) if k == 1 else max(kadane(arr*2), sum(arr)*(k-2) + kadane(arr*2)) % (10**9+7)
