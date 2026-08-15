
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        best = 0
        left = 0
        maxcount = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right] , 0) + 1
            maxcount = max(maxcount, freq[s[right]])

            while (right - left + 1) - maxcount > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best


        