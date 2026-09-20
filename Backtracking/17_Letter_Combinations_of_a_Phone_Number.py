from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        table ={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if not digits:
            return []
        path =[]
        result =[]
        def helper(i):
            
            if len(path) == len(digits):
                result.append("".join(path))
                return
            for letter in table[digits[i]]:
                path.append(letter)
                helper(i+1)
                path.pop()
            
        helper(0)
        return result