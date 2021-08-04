class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n_boxes = len(boxes)
        pos = [i for i,j in enumerate(boxes) if j == '1']
        allsum = sum(pos)
        n_balls = len(pos)
        
        ans = []
        left_sum = 0
        left_ball = 0
        for k in range(len(boxes)):
            
            left_sum -= left_ball
            if boxes[k] == '1':
                left_ball += 1
            
            ans.append(allsum - n_balls*k - 2*left_sum)
            
        return ans
