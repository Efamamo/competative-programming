class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.time={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, in_time=self.checkin[id]
        tr=(start,stationName)
        time=t-in_time
        if tr not in self.time:
            self.time[tr] =[0,0]
        self.time[tr][0]+=time
        self.time[tr][1]+=1



        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count=self.time[(startStation,endStation)]
        return total/count
        


        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)