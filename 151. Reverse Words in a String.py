"""
Question: 151. Reverse Words in a String
Status: Done
Difficulty: Easy
Author: iamss
Created: 19/08/25
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.strip().split() if word != ' ']
        return ' '.join(words[::-1])
