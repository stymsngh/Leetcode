"""
Question: 58. Length of Last Word
Status: Done
Difficulty: Easy
Author: iamss
Created: 19/08/25
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
