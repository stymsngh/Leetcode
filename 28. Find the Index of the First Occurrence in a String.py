"""
Question: 28. Find the Index of the First Occurrence in a String
Status: Done
Difficulty: Easy
Author: iamss
Created: 17/08/25
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay, len_needle = len(haystack), len(needle)
        for i in range(len_hay - len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1