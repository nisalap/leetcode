class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        gaps = [capacity[i] - rocks[i] for i in range(len(capacity))]
        gaps.sort()
        count = 0
        for i in gaps:
            if (additionalRocks - i) >= 0:
                count += 1
                additionalRocks -= i
        return count
