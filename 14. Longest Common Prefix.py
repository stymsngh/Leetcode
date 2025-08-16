"""
Question: 14. Longest Common Prefix
Status: Done
Difficulty: Medium
Author: iamss
Created: 16/08/25
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sorted_strs = sorted(strs, key=len)
        smallest_str = sorted_strs[0]
        lcp = ""
        for i in range(len(smallest_str)):
            key = smallest_str[i]
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] != key:
                    return lcp
            lcp += key
        return lcp