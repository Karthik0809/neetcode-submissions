class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        longest = 0
        maxCount = 0

        for right in range(len(s)):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Highest frequency in the current window
            maxCount = max(maxCount, freq[s[right]])

            # If we need more than k replacements, shrink window
            while (right - left + 1) - maxCount > k:
                freq[s[left]] -= 1
                left += 1

            # Update longest valid window
            longest = max(longest, right - left + 1)

        return longest
        