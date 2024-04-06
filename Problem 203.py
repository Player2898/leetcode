# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val: #if the val is head or all the nodes have the same val
            head = head.next

        if not head:
            return head
        cur = head
        while cur:
            if cur.next and cur.next.val == val: 
                cur.next = cur.next.next #skipping the next node if it is same as val 

            else:
                cur = cur.next
        return head
