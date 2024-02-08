class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0] * (n+2)
        for i in range(len(bookings)):
            res[bookings[i][0]]+=bookings[i][2]
            res[bookings[i][1]+1]-=bookings[i][2]
        for i in range(1,len(res)):
            res[i]+=res[i-1]
        return res[1:n+1]
        