"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Problem: Can a person attend ALL meetings without conflicts?
        
        Example 1:
        Input: intervals = [(0,30),(5,10),(15,20)]
        Output: False
        Explanation: (0,30) conflicts with (5,10) and (15,20)
        
        Example 2:
        Input: intervals = [(5,8),(9,15)]
        Output: True
        Explanation: No conflicts, can attend both
        
        Note: (0,8) and (8,10) is NOT a conflict (boundary is OK)
        
        Approach:
        1. Sort meetings by start time
        2. Check if any consecutive meetings overlap
        3. If ANY overlap → return False
           If NO overlaps → return True
        """
        
        # ========== EDGE CASE: EMPTY OR SINGLE MEETING ==========
        # If no meetings or only one meeting, no conflicts possible
        if not intervals or len(intervals) <= 1:
            return True
        
        # ========== STEP 1: SORT BY START TIME ==========
        # Sort Interval objects by their start time
        # This allows us to check conflicts between consecutive meetings
        #
        # Example: [(0,30), (5,10), (15,20)]
        # After sort: [(0,30), (5,10), (15,20)]
        # (sorted by start: 0, 5, 15)
        intervals.sort(key=lambda interval: interval.start)
        
        # ========== STEP 2: CHECK FOR CONFLICTS ==========
        # Iterate through consecutive meetings
        for i in range(1, len(intervals)):
            # Get current and previous meeting
            current = intervals[i]      # Current meeting
            previous = intervals[i - 1] # Previous meeting
            
            # --------- CONFLICT CHECK ---------
            # Conflict occurs if: current_start < previous_end
            # NO conflict if: current_start >= previous_end
            #
            # Example 1: current=(5,10), previous=(0,30)
            # 5 < 30? YES → CONFLICT! ❌
            #
            # Example 2: current=(8,10), previous=(0,8)
            # 8 < 8? NO → NO CONFLICT! ✅
            
            if current.start < previous.end:
                # CONFLICT FOUND!
                # Person can't attend both meetings
                return False
        
        # ========== STEP 3: NO CONFLICTS FOUND ==========
        # All consecutive meetings checked, no conflicts detected
        return True