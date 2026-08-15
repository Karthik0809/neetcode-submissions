from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, permutation can't exist
        if len(s1) > len(s2):
            return False

        # Count frequency of all characters in s1
        s1_counts = Counter(s1)
        
        # Count frequency of first window in s2 (size = len(s1))
        count_s2 = Counter(s2[:len(s1)])

        # Check if first window matches s1
        if s1_counts == count_s2:
            return True

        # Slide the window through s2
        for i in range(len(s1), len(s2)):
            # Add new character entering the window from right
            count_s2[s2[i]] += 1

            # Get the character leaving the window from left
            left = s2[i - len(s1)]
            
            # Remove it from window
            count_s2[left] -= 1

            # If character frequency becomes 0, delete it from counter
            if count_s2[left] == 0:
                del count_s2[left]

            # Check if current window matches s1
            if s1_counts == count_s2:
                return True
        
        # No permutation found
        return False
