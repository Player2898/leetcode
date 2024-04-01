# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      #can be done without a nested function as well.
        def sortandmerge(l1,l2):
            #if either of the list is empty return the non-empty list.
            if not l1 or not l2:
                return l1 or l2
            
            if l1.val < l2.val:
                l1.next = sortandmerge(l1.next,l2)
                return l1
            else:
                l2.next = sortandmerge(l1,l2.next)
                return l2
        return sortandmerge(list1,list2)
        
