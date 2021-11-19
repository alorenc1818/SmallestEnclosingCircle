class GameState():
    def __init__(self):
        self.points=[]

    
    def addPoint(self,point, color):
        self.points.append((point,color))
        #print(self.points)

    def getPoints(self):
        return self.points