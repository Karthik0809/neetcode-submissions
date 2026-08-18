class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Problem: Merge overlapping intervals
        
        Example:
        Input: [[1,3],[1,5],[6,7]]
        Output: [[1,5],[6,7]]
        
        Approach:
        1. Sort intervals by start time
        2. Iterate and merge overlapping ones
        3. Return merged intervals
        """
        
        # ========== STEP 1: SORT BY START TIME ==========
        # Sort intervals so we can check overlaps from left to right
        # Example: [[1,3],[1,5],[6,7]] → [[1,3],[1,5],[6,7]] (already sorted)
        #          [[6,7],[1,3],[1,5]] → [[1,3],[1,5],[6,7]] (after sort)
        intervals.sort()
        
        # ========== STEP 2: INITIALIZE RESULT ==========
        # result will store non-overlapping merged intervals
        result = []
        
        # ========== STEP 3: ITERATE AND MERGE ==========
        for start, end in intervals:
            # start = beginning of current interval
            # end = ending of current interval
            
            # Example: [1,3], [1,5], [6,7]
            
            # --------- CHECK: Does current overlap with previous? ---------
            # Overlap occurs if: current_start <= previous_end
            # 
            # Example:
            # [1,3] and [1,5]: 1 <= 3? YES → overlap! ✅
            # [1,3] and [6,7]: 6 <= 3? NO → no overlap ❌
            
            if result and start <= result[-1][1]:
                # YES, OVERLAP! → MERGE
                # result[-1] = previous interval in result
                # result[-1][1] = end of previous interval
                # 
                # Merge: extend the end of previous interval
                # to be the maximum of both ends
                result[-1][1] = max(result[-1][1], end)
                
                # Example:
                # result[-1] = [1, 3]
                # current = [1, 5]
                # max(3, 5) = 5
                # result[-1] becomes [1, 5] ✅
            else:
                # NO OVERLAP → ADD TO RESULT
                # Add current interval as a new interval
                result.append([start, end])
                
                # Example:
                # result was [[1,5]]
                # current is [6,7]
                # result becomes [[1,5], [6,7]] ✅
        
        # ========== STEP 4: RETURN MERGED INTERVALS ==========
        return result