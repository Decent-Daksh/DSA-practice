
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None :
            return head
        prev = None
        curr = head
        nex = head.next
        while nex:
            curr.next = prev
            prev = curr
            curr =nex
            nex =nex.next
        curr.next = prev
        return curr

        