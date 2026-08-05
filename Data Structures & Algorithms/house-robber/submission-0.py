class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_one = 0   # Max money ending at previous house
        prev_two = 0   # Max money 2 houses back

        for current_money in nums:
            # Either rob current + prev_two, or skip current (keep prev_one)
            current_max = max(current_money + prev_two, prev_one)
            
            # Shift
            prev_two = prev_one
            prev_one = current_max

        return prev_one