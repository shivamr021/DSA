class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = float('-inf')
        removal_count = 0

        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                removal_count += 1
                
        return removal_count
            
