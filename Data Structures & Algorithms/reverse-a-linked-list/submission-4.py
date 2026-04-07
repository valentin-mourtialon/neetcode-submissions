# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        it = head
        prev = None
        while it:
            next_copy = it.next
            if prev:
                it.next = prev
            else:
                it.next = None
            prev = it
            it = next_copy
        head = prev
        return head