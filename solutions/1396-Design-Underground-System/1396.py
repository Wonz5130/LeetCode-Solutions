class UndergroundSystem:

    def __init__(self):
        self.enterstation = {}
        self.leavestation = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.enterstation:
            self.enterstation[stationName] = [[id, t]]
        else:
            self.enterstation[stationName].append([id, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.leavestation:
            self.leavestation[stationName] = [[id, t]]
        else:
            self.leavestation[stationName].append([id, t])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res = []
        start = self.enterstation[startStation]
        end = self.leavestation[endStation]
        for i in start:
            for j in end:
                # id相同
                if i[0] == j[0]:
                    res.append(abs(j[1] - i[1]))
        return float(sum(res) / len(res))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)