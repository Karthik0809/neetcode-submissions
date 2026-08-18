class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Problem: Insert a new interval into sorted non-overlapping intervals
        
        Example 1:
        intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output: [[1,6]]
        
        Example 2:
        intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        Output: [[1,2],[3,5],[6,7],[9,10]]
        
        Approach: Three phases
        1. Add all intervals that END BEFORE newInterval STARTS (no overlap)
        2. Merge newInterval with all OVERLAPPING intervals
        3. Add all intervals that START AFTER newInterval ENDS (no overlap)
        """
        
        result = []
        i = 0
        start, end = newInterval  # Unpack new interval
        
        # ========== PHASE 1: ADD NON-OVERLAPPING INTERVALS BEFORE ==========
        # Add all intervals that end BEFORE newInterval starts
        # These don't overlap, so add them as-is
        #
        # Condition: interval[end] < newInterval[start]
        # Example: [1,3] ends at 3, newInterval starts at 5 → 3 < 5? YES → add [1,3]
        
        while i < len(intervals) and intervals[i][1] < start:
            # intervals[i][1] = end of current interval
            # start = start of new interval
            # If current interval ends before new starts → no overlap
            result.append(intervals[i])
            i += 1
        
        # After this loop:
        # result contains all non-overlapping intervals that come BEFORE newInterval
        # i points to first interval that might overlap
        
        # ========== PHASE 2: MERGE OVERLAPPING INTERVALS ==========
        # Merge newInterval with all intervals that overlap with it
        #
        # Overlap occurs when: interval[start] <= newInterval[end]
        # Example: [4,6] starts at 4, newInterval ends at 5 → 4 <= 5? YES → overlap!
        
        while i < len(intervals) and intervals[i][0] <= end:
            # intervals[i][0] = start of current interval
            # end = end of new interval
            # If current interval starts before new ends → overlap!
            
            # Merge: extend the boundaries
            # start = minimum of both starts (take leftmost)
            start = min(start, intervals[i][0])
            # end = maximum of both ends (take rightmost)
            end = max(end, intervals[i][1])
            i += 1
        
        # After this loop:
        # start, end = merged interval boundaries
        # i points to first interval that doesn't overlap
        
        # Add the merged newInterval to result
        result.append([start, end])
        
        # ========== PHASE 3: ADD NON-OVERLAPPING INTERVALS AFTER ==========
        # Add all remaining intervals
        # These don't overlap (come after merged interval)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        # After this loop:
        # result contains all intervals (with newInterval merged)
        
        return result