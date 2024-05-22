#browser history with linked list.
class Listnode:
    def __init__(self,val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Listnode(homepage)

    def visit(self, url: str) -> None:
        #adds the url(nodes) in the form of linked list.
        #note : when a new node is insterted where there is already a connection(eg facebook and youtube) the existence of the following node is left back and cannot be found again(linkedin is added after facebook and connection with youtube is lost).
        node = Listnode(url)
        self.current.next = node
        node.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        #iterating backwards with given steps till one of the condition fails. self.current.prev checks the existence of prev node. Same logic for forward aswell.
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
