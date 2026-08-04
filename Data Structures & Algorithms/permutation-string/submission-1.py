class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        if window_count == s1_count:
            return True
        
        for i in range(len(s1), len(s2)):
            # Add new character
            window_count[s2[i]] += 1
            
            # Remove leftmost character
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Check if match
            if window_count == s1_count:
                return True
        
        return False


        