from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range (len (temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack[-1]
                stack.pop()
                answer[temp] = i - temp
            stack.append(i)
        return answer




       