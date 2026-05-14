# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            head = list2
            return head
        if not list2:
            head = list1
            return head

        if list1.val < list2.val:
            head = list1
            fix = list2
        else:
            head = list2
            fix = list1
        ptr = head
        while ptr:
            # print(
            #     f"ptr.next.val={ptr.next.val if ptr.next else None} <= fix.val={fix.val if fix else None}"
            # )
            if ptr.next and (fix is None or ptr.next.val <= fix.val):
                ptr = ptr.next
            else:
                new_fix = ptr.next
                ptr.next = fix
                ptr = ptr.next
                fix = new_fix

        return head