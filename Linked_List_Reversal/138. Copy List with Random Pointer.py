
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        check={}
        if head is None :
            return None
        def get_copy(node):
            if node is None :
                return None
            if node not in check :
                check[node] = Node(node .val)
            return check[node]    
        while curr is not None:
            curr_1 = get_copy(curr)
            curr_1.next = get_copy(curr.next)
            curr_1.random =  get_copy(curr.random)
            curr = curr.next
        return check[head]

