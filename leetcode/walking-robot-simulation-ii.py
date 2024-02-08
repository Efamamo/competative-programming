class Robot:
    DIRECTIONS = {(1,0):"East",(0,1):"North",(-1,0):"West",(0,-1):"South"}

    def __init__(self, width: int, height: int):
        self.max_y = height-1
        self.max_x = width -1 
        self.pos = [0,0]
        self.dir = [0,-1]
        self.moves = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moves += num
        self.moved = True
       

    def getPos(self) -> List[int]:
        if self.moves:
            self.move( self.moves % (2*(self.max_y )+ 2*self.max_x))
            self.moves = 0

        return self.pos

    def getDir(self) -> str:
        if self.moves:
            self.move( self.moves % (2*(self.max_y )+ 2*self.max_x))
            self.moves = 0

        return Robot.DIRECTIONS[(self.dir[0],self.dir[1])] if self.moved  else "East"

    def move(self, num:int) -> None:
        dx,dy = map(lambda x: num*x,self.dir)
        self.pos[0] += dx
        self.pos[1] += dy 

        if self.pos[0] > self.max_x or self.pos[0] < 0:
            self.change_direction()
            if  self.pos[0] < 0:
                self.pos[0], overflow = 0, -self.pos[0]
                self.move(overflow)
            else:
                self.pos[0], overflow = self.max_x, self.pos[0] - self.max_x
                self.move(overflow)

        elif self.pos[1] > self.max_y or self.pos[1] < 0:
            self.change_direction()

            if  self.pos[1] < 0:
                self.pos[1], overflow = 0, -self.pos[1]
                self.move(overflow)
            else:
                self.pos[1], overflow = self.max_y, self.pos[1] - self.max_y
                self.move(overflow)

    
    def change_direction(self) -> None:            
        self.dir[1] *= -1
        self.dir[0], self.dir[1] = self.dir[1], self.dir[0]
    

