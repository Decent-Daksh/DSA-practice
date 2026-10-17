# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None :
            return head
        node_1 = head
        node_2 = head.next
        left , right = node_1, node_2
        while  right and right.next:
            left.next = right.next
            left = left.next
            right.next = left.next
            right = right.next
        
        left.next = node_2
        return head