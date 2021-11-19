import pygame as p
import random as rn
from GameState import GameState
from findCircle import *
#from Button import Button
WIDTH=HEIGHT=1024
MAX_FPS=15
POINT_SIZE=10
CIRCLE_WIDTH=5

def randomColor():
    return (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))

def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=GameState()
     
    running=True
    simulating=False
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type==p.MOUSEBUTTONDOWN:
                if not simulating:
                    location=p.mouse.get_pos()
                    newPoint=(location[0],location[1])
                    gs.addPoint(newPoint,randomColor())
                else:
                    pass
        drawBoard(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen,gs):
    for point in gs.points:
        p.draw.circle(screen,point[1],point[0],POINT_SIZE)

    points=gs.points
    n=len(points)
    circle=0
    if n>=3:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and k!=i:
                        c=findCircle(points[i][0],points[j][0],points[k][0])
                        flag=True
                        for point in points:
                            if not isInCircle(c,point):
                                flag=False
                        if flag:
                            circle=c
        
        #if flag:       

        p.draw.circle(screen,points[0][1], circle[0], circle[1],CIRCLE_WIDTH)

   

main()