# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        dummy = ListNode(0,head)
        curr = dummy
        count = 0
        l = r = prev = nex = None
        while count < right+1:
            if count==left-1:
                prev = curr
                l = curr.next
            if count == right:
                r = curr
                nex = curr.next
            curr = curr.next 
            count +=1
        curr = l
        earlier = None
        while curr is not nex:
            next_temp = curr.next
            curr.next = earlier
            earlier = curr
            curr = next_temp
        prev.next = r
        l.next = nex
        return dummy.next
