from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left , right = 0 , len(s)-1
        while left<= right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right-=1
        return s


# this the recursive approach
from typing import List
class Solution:
    def reverse_string(self , s:List[str]):
        if len(s) == 1:
            return s[0]
        
        return (self.reverse_string(s[1:])+ s[0])

