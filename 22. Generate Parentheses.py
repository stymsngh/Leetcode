"""
Question: 22. Generate Parentheses
Status: Done
Difficulty: Medium
Author: iamss
Created: 21/08/25
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        oc, cc = 0, 0
        ans = []
        self.gen(n, oc, cc, ans, [])
        return ans

    def gen(self, n: int, oc: int, cc: int, ans: List[str], temp: List[str]) -> None:
        if len(temp) == n * 2:
            ans.append(''.join(temp))
            return ans

        if oc < n:
            temp.append('(')
            self.gen(n, oc + 1, cc, ans, temp)
            temp.pop()

        if cc < oc:
            temp.append(')')
            self.gen(n, oc, cc + 1, ans, temp)
            temp.pop()
