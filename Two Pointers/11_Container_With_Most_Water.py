from typing import List
class Solution:
    def container(self, height):
        left , right  = 0 , len(height)-1
        maxi = 0

        while left<right:
            vol = min(height[left], height[right]) * (right-left)
            maxi  = max(vol, maxi)
            if height[left]<height[right]:
                left +=1
            else:
                right -= 1

        return maxi
