from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
     
        path = []
        result =[]
        def helper(open, close):
            if open==close and open==n:
                result.append("".join(path))
                return
            if open<n:
                path.append('(')
                helper(open+1, close)
                path.pop()
            if close<open:
                path.append(')')
                helper(open, close+1)
                path.pop()
        helper(0,0)
        return result