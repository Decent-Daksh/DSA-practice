from typing import List
class Solution:
    def reverse_string(self , s:List[str]):
        if len(s)== 0:
            return ''
        return (self.reverse_string(s[1:])+ s[0])
