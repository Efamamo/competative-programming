class Bitset:

    def __init__(self, size: int):
        self.bits=["0"]*size
        self.counter=0
        self.rcounter=0
        self.rev_bts=["1"]*size

    def fix(self, idx: int) -> None:
        if self.bits[idx]=="0":
            self.bits[idx]="1"
            self.counter+=1

        if self.rev_bts[idx]=="1":
            self.rev_bts[idx]="0"
            self.rcounter+=1


    def unfix(self, idx: int) -> None:
        if self.bits[idx]=="1":
            self.bits[idx]="0"
            self.counter-=1

        if self.rev_bts[idx]=="0":
            self.rev_bts[idx]="1"
            self.rcounter-=1

    def flip(self) -> None:
        key=self.bits
        self.bits=self.rev_bts
        self.rev_bts=key
        self.counter=len(self.bits)-self.counter

        

    def all(self) -> bool:
        return self.counter==len(self.bits)
        

    def one(self) -> bool:
        return self.counter>0
        
        

    def count(self) -> int:
        return self.counter
        

    def toString(self) -> str:
        return "".join(self.bits)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()