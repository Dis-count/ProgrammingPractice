import random

class Table():
 
    location = [([1] * 9) for i in range(5)]
    room = []
    def inIt(self):
        location = [([1] * 9) for i in range(5)]
        for i in range(5):
            location[i][0] = 0
        #标志特殊位置
        location[0][0] = 1
        location[1][0] = 1
        location[0][8] = 0
        location[1][5] = 0
        location[3] = [0] * 9
        location[3][1] = 1
        location[3][2] = 1
        location[4][4] = 0
        location[4][5] = 0
        location[4] = [0] * 9
        for i in range(5):
            location[4][i] = 1
 
        self.location = location
    #生成随机列表
    def generateRandomList(self):
        #去掉空位
        nothing = []
        nothing.append(1)
        nothing.append(13)
        nothing.append(32)
        nothing.append(31)
        nothing.append(30)
        nothing.append(29)
        nothing.append(28)
        nothing.append(27)
        nothing.append(35)
        nothing.append(36)
        nothing.append(37)
        nothing.append(38)
        nothing.append(44)
 
        self.room = []
        i = 0
        while len(self.room) < 31:
            m = int(random.random()*100 % 44 + 1)
            if m not in self.room and m not in nothing:
                self.room.append(m)
                i += 1
        return self.room
    def generateLocal(self):
        #随机列表对座位赋值
        for i in range(5):
            for j in range(9):
                if self.location[i][j] == 1:
                    self.location[i][j] = self.room.pop(0)
        return self.location
    def getTable(self):
        self.inIt()
        self.generateRandomList()
 
        return self.generateLocal()