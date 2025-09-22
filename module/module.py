andset = [(0,0,0),(0,1,0),(1,0,0),(1,1,1)]
orset = [(0,0,0),(0,1,1),(1,0,1),(1,1,1)]




class myandgate:
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.b = 0.5
        self.lr = 0.001
    def annd(self,x1,x2):
        return (x1*self.w1+x2*self.w2+self.b)
    def backward(self,x1,x2,y, yhat):
        self.b = self.b+2*self.lr*(y-yhat)
        self.w1 = self.w1+2*self.lr*x1*(y-yhat)
        self.w2 = self.w2+2*self.lr*x2*(y-yhat)
    
            
def getloss(y,yhat):
    return (y - yhat)**2
        
andgate = myandgate()
epoch = 1000
for i in range(epoch):
    loss=0
    for x1, x2, y in andset:
        y_pred = andgate.annd(x1, x2)
        andgate.backward(x1,x2,y,y_pred)
        print(y, y_pred)
        loss+=getloss(y,y_pred)
        print("loss:", loss/4)