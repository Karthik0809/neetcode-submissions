from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

         # Count characters in s1
        count_s1 = Counter(s1) 
 
        # Count characters in the first window of s2
        count_s2 = Counter(s2[:len(s1)]) 
 
        # If first window is an anagram of s1
        if count_s1 == count_s2: 
            return True 
 
        # Slide the window through s2
        for i in range(len(s1), len(s2)): 

            # Add the new character entering the window
            count_s2[s2[i]] += 1 
 
            # Remove the character leaving the window
            left = s2[i - len(s1)] 
            count_s2[left] -= 1 
 
            # Remove character from Counter if its count becomes 0
            if count_s2[left] == 0: 
                del count_s2[left] 
 
            # Check if current window is an anagram of s1
            if count_s1 == count_s2: 
                return True

        return False



