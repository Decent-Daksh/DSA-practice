from typing import List
class Solution:
    def permutaionInString(s1:List , s2:List)-> bool:
        if len(s1)>len(s2):
            return False
        check={}
        window={}
        left = 0
        for i in range(len(s1)):
            check[s1[i]]= check.get(s1[i],0)+ 1
        for i in range(len(s1)):
            window[s2[i]]= window.get(s2[i],0)+ 1
        if window == check:
            return True
        for i in range(len(s1),len(s2)):
            window[s2[i]] = window.get(s2[i],0)+1
            window[s2[left]] = window.get(s2[left])-1
            if window[s2[left]]==0:
                del window[s2[left]]
            left +=1
            if window == check:
                return True
        return False

        