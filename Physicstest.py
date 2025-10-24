import math
import pygame
from pygame import gfxdraw

p1y = float(200) #y position
p1x = float(400) #x position
# p1dir = float(90) # angle 0 being up 
p1speedx = float(1.2) #x fart
p1speedy = float(0) #y fart
p1mass = int(10000000000000) #massa

f1 = int()

# sin x cos y

KonstG = 6.674*float(10**-11) #konstanten G
dist = float()
ang1 = float()
ang2 = float()

p2y = float(400)
p2x = float(400)
# p2dir = float(270)
p2speedx = float(-1.2)
p2speedy = float(0)
p2mass = int(10000000000000)

pixelx = 0
pixely = 0

screenwidth = 800
screenheight = 800

coloureq = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event betyder att användaren klickade på X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bakgrundsfärg
    screen.fill("black")

    # renderering
    i = 0
    j = 0
    while i < screenwidth:
        while j < screenheight:
            coloureq = int(255-(0.001*math.hypot(abs(i-400),abs(j-400))**2))
            if coloureq < 0:
                coloureq = 0
            if coloureq > 255:
                coloureq = 255
            gfxdraw.pixel(screen, i+int(pixelx%5), j+int(pixely%5), ((coloureq), 200-int(coloureq*0.5), 200))
            j += 6
        i += 6
        j = 0
    pygame.draw.circle(screen, "red", (p1x, p1y), 30)
    pygame.draw.circle(screen, "blue", (p2x, p2y), 30)

    # updaterar displayen
    pygame.display.flip()

    # uträkningar

    dist = math.hypot((p1x-p2x),(p1y-p2y)) #hittar distansen mellan planeterna
    ang1 = math.atan2((p2y-p1y),(p2x-p1x)) #hittar vinkeln mellan dem
    f1 = (KonstG*p1mass*p2mass)/dist**2 #kraften mellan planeterna
    if dist <= 60: #gör så att planeterna studsar
        f1 *= -1
    
    p1speedx = p1speedx + math.cos(ang1)*f1/p1mass #räknar ut farterna i x och y
    p1speedy = p1speedy + math.sin(ang1)*f1/p1mass
    '''if p1x >= 770 or p1x <= 30: #gör så att planeten studsar på väggarna
        p1speedx *= -1
    if p1y >= 770 or p1y <= 30:
        p1speedy *= -1'''
    p1x = p1x + p1speedx #ändrar positionen med farten
    p1y = p1y + p1speedy

    ang2 = math.atan2((p1y-p2y),(p1x-p2x))
    p2speedx = p2speedx + math.cos(ang2)*f1/p2mass
    p2speedy = p2speedy + math.sin(ang2)*f1/p2mass
    '''if p2x >= 770 or p2x <= 30:
        p2speedx *= -1
    if p2y >= 770 or p2y <= 30:
        p2speedy *= -1'''
    p2x = p2x + p2speedx
    p2y = p2y + p2speedy

    pixelx = pixelx - p2x
    pixely = pixely - p2y

    p1x = p1x + 400 - p2x
    p1y = p1y + 400 - p2y
    p2x = 400
    p2y = 400
    clock.tick(60)  # 60 fps
print(dist)
print(f1)
print(math.degrees(ang1))
print(math.cos(ang1)*f1)
print(math.sin(ang1)*f1)
pygame.quit()