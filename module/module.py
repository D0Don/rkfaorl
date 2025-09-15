andset = [(0,0,0),(0,1,0),(1,0,0),(1,1,1)]
orset = [(0,0,0),(0,1,1),(1,0,1),(1,1,1)]

class myandgate:
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.b = 0.5
    def annd(self,x1,x2):
        return (x1*self.w1+x2*self.w2+self.b)
        
andgate = myandgate()


def getloss(y,yhat):
    return (y-yhat)**2
for i in range(4):
    print(getloss(andset[i][2],andgate.annd(andset[i][0],andset[i][0])))

