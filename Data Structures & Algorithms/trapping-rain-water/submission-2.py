class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        
        # Maximum height seen from the left and right
        leftmax = height[l]
        rightmax = height[r]

        res = 0

        while l < r:

            # Process the side with the smaller maximum
            if leftmax < rightmax:
                l += 1

                # Update left maximum
                leftmax = max(leftmax, height[l])

                # Water at current position = left max - current height
                res += leftmax - height[l]

            else:
                r -= 1

                # Update right maximum
                rightmax = max(rightmax, height[r])

                # Water at current position = right max - current height
                res += rightmax - height[r]

        return res
            