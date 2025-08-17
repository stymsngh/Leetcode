"""
Question: 49. Group Anagrams
Status: Done
Difficulty: Medium
Author: iamss
Created: 17/08/25
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sorted_word = ''.join(sorted(string))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(string)
            else:
                anagrams[sorted_word] = [string]

        return list(anagrams.values())