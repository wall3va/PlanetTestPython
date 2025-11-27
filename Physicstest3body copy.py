import math
import pygame
from pygame import gfxdraw

dictionary = dict()
numberofplanets = int(3)
#röd
dictionary["p1y"] = float(200) #y position
dictionary["p1x"] = float(400) #x position
# p1dir = float(90) # angle 0 being up 
dictionary["p1speedx"] = float(1.2) #x fart
dictionary["p1speedy"] = float(0) #y fart
dictionary["p1mass"] = int(10000000000000) #massa

f = float()

#grön
dictionary["p3y"] = float(400)
dictionary["p3x"] = float(200)
dictionary["p3speedx"] = float(0)
dictionary["p3speedy"] = float(-1.2)
dictionary["p3mass"] = int(10000000000000)

# sin x cos y

KonstG = 6.674*float(10**-11) #konstanten G
ang1 = float()
ang2 = float()

# blå
dictionary["p2y"] = float(400)
dictionary["p2x"] = float(400)
# p2dir = float(270)
dictionary["p2speedx"] = float(-1.2)
dictionary["p2speedy"] = float(0)
dictionary["p2mass"] = int(10000000000000)

pixelx = 0
pixely = 0

factorial2 = int(1)
for z in range(1, (numberofplanets-2)+1):
    factorial2 *= z

factorial = int(1)
for y in range(1, numberofplanets + 1):
    factorial *= y

screenwidth = 800
screenheight = 800

def planet_calc(functiondictionary, a, b):
    a = str(a)
    b = str(b)
    dist = math.hypot((functiondictionary[f"p{a}x"]-functiondictionary[f"p{b}x"]),(functiondictionary[f"p{a}y"]-functiondictionary[f"p{b}y"])) #hittar distansen mellan planeterna
    ang1 = math.atan2((functiondictionary[f"p{b}y"]-functiondictionary[f"p{a}y"]),(functiondictionary[f"p{b}x"]-functiondictionary[f"p{a}x"])) #hittar vinkeln mellan dem i förhålande till planet 1
    ang2 = math.atan2((functiondictionary[f"p{a}y"]-functiondictionary[f"p{b}y"]),(functiondictionary[f"p{a}x"]-functiondictionary[f"p{b}x"])) #räknar ut vinkeln mellan planeterna i förhållande till planet 2
    f = (KonstG*functiondictionary[f"p{a}mass"]*functiondictionary[f"p{b}mass"])/dist**2 #kraften mellan planeterna
    if dist <= 60: #gör så att planeterna studsar
        f *= -1

    functiondictionary[f"p{a}speedx"] = functiondictionary[f"p{a}speedx"] + math.cos(ang1)*f/functiondictionary[f"p{a}mass"] #räknar ut farterna för planet 1 i x och y
    functiondictionary[f"p{a}speedy"] = functiondictionary[f"p{a}speedy"] + math.sin(ang1)*f/functiondictionary[f"p{a}mass"]
    functiondictionary[f"p{b}speedx"] = functiondictionary[f"p{b}speedx"] + math.cos(ang2)*f/functiondictionary[f"p{b}mass"] #räknar ut farterna för planet 2 i x och y
    functiondictionary[f"p{b}speedy"] = functiondictionary[f"p{b}speedy"] + math.sin(ang2)*f/functiondictionary[f"p{b}mass"]

    '''if p1x >= 770 or p1x <= 30: #gör så att planeten studsar på väggarna
        p1speedx *= -1
    if p1y >= 770 or p1y <= 30:
        p1speedy *= -1'''
    '''if p2x >= 770 or p2x <= 30:
        p2speedx *= -1
    if p2y >= 770 or p2y <= 30:
        p2speedy *= -1'''
    return (functiondictionary)
    
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

    pixelx = pixelx - dictionary["p1x"]
    pixely = pixely - dictionary["p1y"]

    pygame.draw.circle(screen, "red", (dictionary["p1x"], dictionary["p1y"]), 30)
    pygame.draw.circle(screen, "blue", (dictionary["p2x"], dictionary["p2y"]), 30)
    pygame.draw.circle(screen, "green", (dictionary["p3x"], dictionary["p3y"]), 30)

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
    

    # updaterar displayenMicrosoft.QuickAction.Bluetooth
    pygame.display.flip()

    #uträkningar
    for n in range(1, int(factorial/(1*(factorial2)) + 1)):
        for t in range (n + 1, numberofplanets + 1):
            dictionary = planet_calc(dictionary, n, t)

    for n in range(1, numberofplanets + 1):
        dictionary[f"p{n}x"] = dictionary[f"p{n}x"] + dictionary[f"p{n}speedx"] #ändrar positionen med farten
        dictionary[f"p{n}y"] = dictionary[f"p{n}y"] + dictionary[f"p{n}speedy"]

    for n in range(2, numberofplanets + 1):
        dictionary[f"p{n}x"] = dictionary[f"p{n}x"] + screenwidth/2 - dictionary["p1x"]
        dictionary[f"p{n}y"] = dictionary[f"p{n}y"] + screenheight/2 - dictionary["p1y"]
    dictionary["p1x"] = screenwidth/2
    dictionary["p1y"] = screenheight/2

    # renderering



    clock.tick(60)  # 60 fps

pygame.quit()