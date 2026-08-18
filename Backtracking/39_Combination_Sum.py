from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(path , start ,remain):
            if remain == 0:
                result.append(path[:])
                return
            for i in range(start , len(candidates)):
                path.append(candidates[i])
                remain -= candidates[i]

                if remain >= 0:
                    backtrack(path , i, remain)

                remain += candidates[i]
                path.pop()

        backtrack(path , 0 , target)
        return result
            
