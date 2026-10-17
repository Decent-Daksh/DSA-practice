''' Structure of Linked List Node
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def flatten(self, head):
        # code here
        def merge(a,b):
            if b is None:
                return a
            one , two =a , b
            while one.bottom is not None and two is not None:
                if one.bottom.data< two.data:
                    one = one.bottom
                else:
                    next_val_1 , next_val_2 = one.bottom,two.bottom
                    one.bottom =two
                    one = one.bottom
                    one.bottom = next_val_1
                    
                    two = next_val_2
            if two:
                one.bottom = two
            return a
        heads = []
        curr = head
        while curr:
            heads.append(curr)
            curr = curr.next
        
        def solve(lo, hi):
            if lo ==hi:
                return heads[lo]
            mid = lo+(hi-lo)//2
            left = solve(lo,mid)
            right = solve(mid+1,hi)
            return merge(left,right)
        return solve(0,len(heads)-1)
        