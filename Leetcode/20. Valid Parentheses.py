"""
Question: 20. Valid Parentheses
Status: Done
Difficulty: Easy
Author: iamss
Created: 16/08/25
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        paran_mapper = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top_paran = stack[-1]
                    if paran_mapper[char] != top_paran:
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0
