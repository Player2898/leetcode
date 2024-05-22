#designing a Doubly-Linked list using index to acces the elements.
class Listnode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        #creating two dummy listnodes to handle index edge cases incase that index does not exist.
        self.left = Listnode(0)
        self.right = Listnode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            #decrementing the index through every iteration till the desired index is reached.
            index -= 1 
        
        #we also need to make sure that the cur node did not reach the dummy right node.
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
        
    def addAtHead(self, val: int) -> None:

        #left dummy makes it easier to add the head node and right dummy to add at tail.
        node, prev, next = Listnode(val), self.left, self.left.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node 
        
    def addAtTail(self, val: int) -> None:
        node, prev, next = Listnode(val), self.right.prev, self.right
        next.prev = node
        node.next = next
        node.prev = prev
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, prev = Listnode(val), cur.prev
            prev.next = node
            node.prev = prev
            node.next = cur
            cur.prev = node
    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            prev, next = cur.prev, cur.next
            prev.next = cur.next 
            next.prev = cur.prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
