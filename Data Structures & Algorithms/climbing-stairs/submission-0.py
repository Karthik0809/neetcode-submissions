class Solution:
    def climbStairs(self, n: int) -> int:
        prev_one = 1   # Ways to reach previous stair
        prev_two = 1   # Ways to reach 2 stairs back

        for _ in range(n - 1):
            current = prev_one + prev_two
            prev_two = prev_one
            prev_one = current

        return prev_one