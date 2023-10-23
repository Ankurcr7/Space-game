import pygame
import random
import math
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((1000,800))

backgroundimg=pygame.image.load("C:/Users/User/Documents/GitHub/Space-game/Space game/kai-pilger-Ef6iL87-vOA-unsplash.jpg")
backgroundimg2=pygame.image.load("C:/Users/User/Documents/GitHub/Space-game/Space game/space-galaxy-background.jpg")

mixer.music.load('C:/Users/User/Documents/GitHub/Space-game/Space game/music.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

pygame.display.set_caption("C:/Users/User/Documents/GitHub/Space-game/Space game/SPACE MAN")
icon=pygame.image.load("C:/Users/User/Documents/GitHub/Space-game/Space game/launch.png")
pygame.display.set_icon(icon)


playerimg=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/space-invaders.png')
playerx=468
playery=700
pcx=0
pcy=0

enemy1=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/alien (1).png')
enemy2=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/alien.png')
enemy3=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/space-ship.png')
enemyx=random.randint(64,936)
enemyy=64
ey=0.4

bulletp=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/bullet (1).png')
bullete=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/bullet (3).png')
bulletx=0
bullety=690
bullx=0
bully=1.6
bulletstate="ready"


bulletpp=pygame.image.load('C:/Users/User/Documents/GitHub/Space-game/Space game/bullet (2).png')
bulletppx=0
bulletppy=690
bullppx=0
bullppy=1.6
bulletbigstate="r"

scorevalue=0
font=pygame.font.Font('freesansbold.ttf',32)
tx=10
ty=10

lifevalue=3
lifefont=pygame.font.Font('freesansbold.ttf',32)
lx=890
ly=10


over=pygame.font.Font('freesansbold.ttf',64)


def showscore(x,y):
    score=font.render("Score: "+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))

def live(x,y):
    life=lifefont.render("Life: "+str(lifevalue),True,(255,0,0))
    screen.blit(life,(x,y))

def gameover():
    overfont=over.render("GAME OVER",True,(255,255,255))
    screen.blit(overfont,(300,350))


def player(x,y):
    screen.blit(playerimg,(x,y))

def enemya(x,y):
    screen.blit(enemy2,(x,y))


def enemy(x,y):
    screen.blit(enemy1,(x,y))


def fire(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletp,(x,y))


def firee(x,y):
    global bulletbigstate
    bulletbigstate="firee"
    screen.blit(bulletpp,(x,y))


def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow((enemyx-bulletx),2))+ (math.pow((enemyy-bullety),2)))
    
    if distance<27:
        return True
    else:
        return False

def collide(playerx,playery,enemyx,enemyy):
    distx=math.sqrt((math.pow(((enemyx+10)-(playerx-10)),2))+ (math.pow(((enemyy+10)-playery),2)))
    disty=math.sqrt((math.pow(((enemyx-10)-(playerx+10)),2))+ (math.pow(((enemyy+10)-playery),2)))
    if distx<27 or disty<27:
        return True
    else:
        return False

run=True
while run:
    if scorevalue<10:
        screen.blit(backgroundimg,(-400,-500))
    if scorevalue>=10:
        screen.blit(backgroundimg2,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pcx=-0.5
            
            if event.key==pygame.K_RIGHT:
                pcx=0.5
            
            if event.key==pygame.K_UP:
                pcy=-0.5
            if event.key==pygame.K_DOWN:
                pcy=0.5
                

            if event.key==pygame.K_SPACE:
                if bulletstate=="ready":
                    bulletsound= mixer.Sound('C:/Users/User/Documents/GitHub/Space-game/Space game/blaster-2-81267.mp3')
                    bulletsound.play()
                    bulletx=playerx
                    bullety=playery
                    fire(bulletx,bullety)
            
            if event.key==pygame.K_RCTRL:
                if bulletbigstate=="r":
                    bulletsound1= mixer.Sound('C:/Users/User/Documents/GitHub/Space-game/Space game/laser-gun-81720.mp3')
                   
                    bulletsound1.play()
                    bulletppx=playerx
                    bulletppy=playery
                    firee(bulletppx,bulletppy)

            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                pcx=0
                pcy=0

        
        

    if lifevalue>0:

        playerx+=pcx
        playery+=pcy

        if playerx<=0:
            playerx=0
        elif playerx>=936:
            playerx=936

        elif playery<=0:
            playery=0
        elif playery>=736:
            playery=736


        enemyy+=ey

        if enemyy>=864:
            enemyy=-32
            # scorevalue-=1
            enemyx=random.randint(64,936)



        coll=collision(enemyx,enemyy,bulletx,bullety)
        if coll:
            explodesound= mixer.Sound('C:/Users/User/Documents/GitHub/Space-game/Space game/explosion-6055.mp3')
            explodesound.play()
            bullety=playery
            bulletstate="ready"
            scorevalue+=1

            enemyx=random.randint(64,936)
            enemyy=64


        collo=collision(enemyx,enemyy,bulletppx,bulletppy)
        if collo:
            explodesound= mixer.Sound('C:/Users/User/Documents/GitHub/Space-game/Space game/explosion-6055.mp3')
            explodesound.play()
            bulletppy=playery
            bulletbigstate="r"
            scorevalue+=1
            enemyx=random.randint(64,936)
            enemyy=64

        coli=collide(playerx,playery,enemyx,enemyy)
        if coli:
            lifevalue-=1
            enemyx=random.randint(64,936)
            enemyy=64
            playerx=468
            playery=700


        if bullety<=0:
            # bullety=playery
            bulletstate="ready"
    

        if bulletstate == "fire":
            fire(bulletx,bullety)
            bullety-=bully


        if bulletppy<=0:
            # bullety=playery
            bulletbigstate="r"
    

        if bulletbigstate == "firee":
            firee(bulletppx,bulletppy)
            bulletppy-=bullppy


    
    
        if scorevalue==-1:
            gameover()
        if scorevalue<=-2:
            break

    
        player(playerx,playery)

        if scorevalue<10:
            enemy(enemyx,enemyy)

        if scorevalue>=10:
            enemya(enemyx,enemyy)

        showscore(tx,ty)
        live(lx,ly)

    if lifevalue<=0:
        screen.fill((0,0,0))
        showscore(tx,ty)
        live(lx,ly)
        gameover()


    pygame.display.update()
