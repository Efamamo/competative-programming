class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size += 1
        

    def pop(self) -> int:
        if not self.empty():

            while self.size > 1:
                x = self.queue1.popleft()
                self.queue2.append(x)
                self.size -=1
          
           
            y =  self.queue1.popleft()
            self.size = 0
            while self.queue2:
                x = self.queue2.popleft ()
                self.queue1.append(x)
                self.size +=1

            return y
        
    def top(self) -> int:
        if not self.empty():
            return self.queue1[-1]
        

    def empty(self) -> bool:
        
        if not self.queue1:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()