import pygame as p
import random as rn
from GameState import GameState
from findCircle import *
from Button import Button
WIDTH=HEIGHT=1024
MAX_FPS=15
POINT_SIZE=10
CIRCLE_WIDTH=5
color_light = (170,170,170)

def randomColor():
    return (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))

def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    gs=GameState()
     
    running=True
    color=(0,0,0)
    smallfont = p.font.SysFont('Corbel',35)
    infoText="Entering points"
    textSurface = smallfont.render(infoText , True , color)

    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type==p.MOUSEBUTTONDOWN:
                if not gs.simulating:
                    location=p.mouse.get_pos()
                    newPoint=(location[0],location[1])
                    gs.addPoint(newPoint,randomColor())
                else:
                    pass
            elif e.type == p.KEYDOWN:
                if e.key == p.K_SPACE:
                    if gs.simulating==False:
                        infoText="Steps of the algorithm"
                        textSurface=smallfont.render(infoText , True , color)
                        gs.simulating=True
                    else:
                        infoText="Entering Points"
                        textSurface=smallfont.render(infoText , True , color)
                        gs.simulating=False
                elif e.key==p.K_RIGHT:
                    if gs.simulating:
                            gs.next()
                    
        drawBoard(screen,gs,gs.simulating)
        screen.blit(textSurface , (WIDTH/2-100,0))
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen,gs,simulating):
    screen.fill(p.Color("white"))
    #button
    #p.draw.rect(screen,color_light,[WIDTH/2-50,HEIGHT-50,25,25])
    for point in gs.points:
        p.draw.circle(screen,point[1],point[0],POINT_SIZE)
    
    if simulating:
        triplet=gs.tripleToCheck
        if(triplet[0]!=triplet[1] and triplet[1]!=triplet[2] and triplet[2]!=triplet[1]):
            #print(triplet)
            points=gs.points
            n=len(points)
            circle=0
            if n>=3:
                circle=findCircleFromTriple(points[triplet[0]][0],points[triplet[1]][0],points[triplet[2]][0])
                #print(circle)
                p.draw.circle(screen,points[0][1], circle[0], circle[1],CIRCLE_WIDTH)



main()