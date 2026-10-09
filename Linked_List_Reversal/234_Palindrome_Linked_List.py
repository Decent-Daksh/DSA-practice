
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        curr = head
        prev = None
        while curr!=slow:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        if fast ==None:
            one =curr
            two = prev
        else:
            one = curr.next
            two = prev
        while one and two:
            if one.val == two.val:
                one = one.next
                two = two.next
            else:
                return False
        return True
        

        

        