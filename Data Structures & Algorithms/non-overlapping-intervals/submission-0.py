class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Problem: Find MINIMUM intervals to REMOVE to make rest non-overlapping
        
        Key Difference from Previous Problems:
        
        ✅ Merge Intervals:
           Input: overlapping intervals
           Goal: MERGE them together
           Output: merged intervals list
        
        ✅ Insert Interval:
           Input: sorted non-overlapping intervals + new interval
           Goal: INSERT and MERGE if needed
           Output: list with inserted interval
        
        ❌ Non-overlapping Intervals:
           Input: possibly overlapping intervals
           Goal: REMOVE minimum count to make non-overlapping
           Output: NUMBER of intervals to remove (not the intervals themselves!)
        
        Example:
        Input: [[1,2],[2,4],[1,4]]
        Which to keep? Keep [1,2] and [2,4] (non-overlapping)
        Which to remove? Remove [1,4]
        Output: 1 (removed 1 interval)
        
        Approach: GREEDY
        - Sort by END time (ascending)
        - Greedily keep intervals that end earliest
        - This leaves most room for future intervals
        - Count how many we skip (those are the overlapping ones)
        """
        
        # ========== STEP 1: SORT BY END TIME ==========
        # Sort intervals by their END point (second value)
        # Why? Intervals ending earlier are less likely to overlap with future ones
        #
        # Example: [[1,2],[2,4],[1,4]]
        # Ends:     2     4     4
        # After sort by end: [[1,2],[2,4],[1,4]]
        #                     end:  2    4    4
        intervals.sort(key=lambda x: x[1])
        
        # ========== STEP 2: GREEDY SELECTION ==========
        # Keep track of when the LAST KEPT interval ends
        last_end = float('-inf')  # Start with negative infinity (no interval yet)
        
        # Count how many intervals we REMOVE (overlap)
        count = 0
        
        # Iterate through sorted intervals
        for start, end in intervals:
            # start = beginning of current interval
            # end = ending of current interval
            
            # --------- CHECK: Does current overlap with last kept? ---------
            # Overlap if: current_start < last_kept_end
            # Non-overlap if: current_start >= last_kept_end
            #
            # Example: last_end = 2, current = [2,4]
            # 2 >= 2? YES → non-overlapping! ✅
            #
            # Example: last_end = 2, current = [1,4]
            # 1 >= 2? NO → overlapping! ❌
            
            if start < last_end:
                # YES, OVERLAP! → MUST REMOVE ONE
                # Remove the one with LARGER END (wastes more space)
                # Keep the one with SMALLER END (greedy!)
                # The one with smaller end is always the PREVIOUS one
                # (because we sorted by end time)
                # So just increment remove count
                count += 1
            else:
                # NO OVERLAP! → KEEP THIS INTERVAL
                # Update last_end to this interval's end
                last_end = end
        
        # ========== STEP 3: RETURN COUNT ==========
        # Return how many intervals we had to remove
        return count