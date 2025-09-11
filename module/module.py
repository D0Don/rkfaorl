andset = [(0,0,0),(0,1,0),(1,0,0),(1,1,1)]
orset = [(0,0,0),(0,1,1),(1,0,1),(1,1,1)]

def annd(x1,x2):
    w1 = 0.5
    w2 = 0.5
    b = 0
    return (x1*w1+x2*w2+b)//1
def getloss(y,yhat):
    return (y-yhat)**2
for i in range(4):
    print(getloss(andset[i][2],annd(andset[i][0],andset[i][0])))