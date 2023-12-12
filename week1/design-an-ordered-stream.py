class OrderedStream:

    def __init__(self, n: int):
        self.result=[0]*n
        self.pointer=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.result[idKey]=value
        if idKey>self.pointer:
            return []
        while self.pointer<len(self.result) and self.result[self.pointer]:
            self.pointer+=1
        return self.result[idKey:self.pointer]
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)