"""
Question: 3. Longest Substring Without Repeating Characters
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = max(length, right-left+1)
        return length
