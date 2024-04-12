#the objective is to reverse the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using three pointers to re-arrange the link between the linknodes
        Next = None
        Curr = None  
        Prev = None

        Curr = head 

        while Curr != None:
            Next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = Next
        head = Prev
        return head
