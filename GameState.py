class GameState():
    def __init__(self):
        self.points=[]
        self.currentCircle=((0,0),0)
        self.tripleToCheck=(0,0,0)
        self.order=0
        self.simulating=False

    
    def addPoint(self,point, color):
        self.points.append((point,color))
        #print(self.points)

    def getPoints(self):
        return self.points

    def next(self):
        if self.simulating:
            n=len(self.points)
            triple=self.nextCanonicalOrder(self.order,n)
            self.order+=1
            while(self.order<n*n*n and (triple[0]==triple[1] or triple[1]==triple[2] or triple[2]==triple[0])):
                triple=self.nextCanonicalOrder(self.order,n)
                self.order+=1
            
            if(triple[0]>=n or triple[1]>=n or triple[2]>=n):
                self.simulating=False
                self.order=0
                triple=(0,0,0)
            self.tripleToCheck=triple

    def nextCanonicalOrder(self,order,n):
        return (order//(n*n), order//n,order%n)