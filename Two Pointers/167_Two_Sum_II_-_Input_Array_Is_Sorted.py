#array in 1 indexed
from typing import List
class Solution:
    def two_sum(self,number,target):
        left , right  = 0 , len(number)-1

        while left < right:
            sum = number[left]+number[right]

            if target == sum:
                return[left+1 , right+1]
            elif sum < target:
                left+=1
            else:
                right -= 1
        return []

num = [1,2,3,4,5,6,7,8,9]
sol = Solution()
answer = sol.two_sum(num , 9)
print(answer)