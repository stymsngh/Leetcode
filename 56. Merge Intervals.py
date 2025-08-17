"""
Question: 56. Merge Intervals
Status: Done
Difficulty: Medium
Author: iamss
Created: 17/08/25
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        merged = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            prev_interval = merged[-1]
            if sorted_intervals[i][0] <= prev_interval[1]:
                # Merge
                merged[-1][1] = max(merged[-1][1], sorted_intervals[i][1])
            else:
                # Add directly
                merged.append(sorted_intervals[i])
        return merged
