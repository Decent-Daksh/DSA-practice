from typing import List
class Solution:
    def find_the_conbination(n,k):
        path=[]
        result=[]
        def helper(index):
            if len(path)==k:
                result.append(path[:])
                return
            for i in range(index,n+1):
                path.append(i)
                helper(i+1)
                path.pop()
        helper(1)
        return result