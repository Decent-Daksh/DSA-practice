# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def rev(curr):
            end = curr
            for i in range(k):
                end = end.next
                if end is None:
                    return None
            prev_grp =curr
            curr =curr.next
            last = curr
            prev = None
            for i in range (k):
                next_temp = curr.next
                curr.next =prev
                prev = curr
                curr = next_temp
            prev_grp.next = prev
            last.next = curr
            return last
        dummy = ListNode(0,head)
        node = dummy
        while node:
            node = rev(node)
        return dummy.next
        



