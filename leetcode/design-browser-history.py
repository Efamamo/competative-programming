class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        
        

    def visit(self, url: str) -> None:
        now = Node(url)
        self.current.next = now
        now.prev = self.current
        self.current = now
        
        
        

    def back(self, steps: int) -> str:
        i = 0
        while self.current.prev and i<steps:
            self.current = self.current.prev
            i+=1
        
        print(self.current.val)
        return self.current.val
        

    def forward(self, steps: int) -> str:
      
        i = 0
        while self.current.next and i<steps:
            self.current = self.current.next
            i+=1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)