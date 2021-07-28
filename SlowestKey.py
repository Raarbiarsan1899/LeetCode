class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        longest_dur = 0
        slowest_key = 'a'
        prev_time = 0
        for i in range(len(keysPressed)):
            if releaseTimes[i] - prev_time > longest_dur:
                longest_dur = releaseTimes[i] - prev_time
                slowest_key = keysPressed[i]
            elif releaseTimes[i] - prev_time == longest_dur:
                if keysPressed[i] > slowest_key:
                    slowest_key = keysPressed[i]
            prev_time = releaseTimes[i]

        return slowest_key
