# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def merge(left, right):
            
            dummy = ListNode(0,None)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next =left
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = right
                    right= right.next
                    curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            return dummy.next
        
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left =self.sortList(head)
        right =self.sortList(right)
        return merge(left,right)
        
