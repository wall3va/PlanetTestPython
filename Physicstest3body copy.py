import math
import pygame
from pygame import gfxdraw

dictionary = dict()
dictionary["numberofplanets"] = int(0)

f = float()

#funktionen som skapar planeter
def planet_maker(dictionary1, x, y, speedx, speedy, mass, colour):
    dictionary1 ["numberofplanets"] += 1
    planetnumber = dictionary1 ["numberofplanets"]
    print(planetnumber)
    dictionary1 [f"p{planetnumber}x"] = x
    dictionary1 [f"p{planetnumber}y"] = y
    dictionary1 [f"p{planetnumber}speedx"] = speedx
    dictionary1 [f"p{planetnumber}speedy"] = speedy
    dictionary1 [f"p{planetnumber}mass"] = mass
    dictionary1 [f"p{planetnumber}colour"] = colour
    return (dictionary1)

#skapar planeterna (hovra över funktionen för förklaring)
dictionary = planet_maker(dictionary, 200, 600, 0, 0, 100000000000, "red")
dictionary = planet_maker(dictionary, 800, 400, -1.2, 0, 10000000000000, "green")
dictionary = planet_maker(dictionary, 0, 600, 0, 1, 100000000000, "blue")
dictionary = planet_maker(dictionary, 400, 600, 0, -1, 100000000000, "yellow")

KonstG = 6.674*float(10**-11) #konstanten G

pixelx = 0
pixely = 0



screenwidth = 800
screenheight = 800

#funktionen som hittar f mellan 2 planeter
def planet_calc(fdict, a, b):
    a = str(a)
    b = str(b)
    dist = math.hypot((fdict[f"p{a}x"]-fdict[f"p{b}x"]),(fdict[f"p{a}y"]-fdict[f"p{b}y"])) #hittar distansen mellan planeterna
    ang1 = math.atan2((fdict[f"p{b}y"]-fdict[f"p{a}y"]),(fdict[f"p{b}x"]-fdict[f"p{a}x"])) #hittar vinkeln mellan dem i förhålande till planet 1
    ang2 = math.atan2((fdict[f"p{a}y"]-fdict[f"p{b}y"]),(fdict[f"p{a}x"]-fdict[f"p{b}x"])) #räknar ut vinkeln mellan planeterna i förhållande till planet 2
    f = (KonstG*fdict[f"p{a}mass"]*fdict[f"p{b}mass"])/dist**2 #kraften mellan planeterna
    if dist <= 60: #gör så att planeterna studsar på varandra
        f *= -1

    fdict[f"p{a}speedx"] = fdict[f"p{a}speedx"] + math.cos(ang1)*f/fdict[f"p{a}mass"] #räknar ut farterna för planet 1 i x och y
    fdict[f"p{a}speedy"] = fdict[f"p{a}speedy"] + math.sin(ang1)*f/fdict[f"p{a}mass"]
    fdict[f"p{b}speedx"] = fdict[f"p{b}speedx"] + math.cos(ang2)*f/fdict[f"p{b}mass"] #räknar ut farterna för planet 2 i x och y
    fdict[f"p{b}speedy"] = fdict[f"p{b}speedy"] + math.sin(ang2)*f/fdict[f"p{b}mass"]

    return (fdict)
def planet_draw(numb, drawdict):
    pygame.draw.circle(screen, drawdict[f"p{numb}colour"], (drawdict[f"p{numb}x"], drawdict[f"p{numb}y"]), 30)

coloureq = 0


factorial2 = int(1)
for z in range(1, (dictionary["numberofplanets"]-2)+1):
    factorial2 *= z


factorial = int(1)
for y in range(1, dictionary["numberofplanets"] + 1):
    factorial *= y

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

    i = 0
    j = 0

    while i < screenwidth: #ritar bakgrunden
        while j < screenheight:
            coloureq = int(255-(0.001*math.hypot(abs(i-(screenwidth/2)),abs(j-(screenheight/2)))**2))
            if coloureq < 0:
                coloureq = 0
            if coloureq > 255:
                coloureq = 255
            gfxdraw.pixel(screen, i+int(pixelx%5), j+int(pixely%5), ((coloureq), 200-int(coloureq*0.5), 200))
            j += 6
        i += 6
        j = 0

    for n in range(1, dictionary["numberofplanets"] + 1): #ritar planeterna
        planet_draw(n, dictionary) 

    # updaterar displayen
    pygame.display.flip()
    
    #uträkningar för hur många gånger man ska räkna ut krafterna mellan planeterna
    for n in range(1, int(factorial/(1*(factorial2)) + 1)):
        for t in range (n + 1, dictionary["numberofplanets"] + 1):
            dictionary = planet_calc(dictionary, n, t)
            print(f"{n}-{t}")
    for n in range(1, dictionary["numberofplanets"] + 1):
        dictionary[f"p{n}x"] = dictionary[f"p{n}x"] + dictionary[f"p{n}speedx"] #ändrar positionen med farten
        dictionary[f"p{n}y"] = dictionary[f"p{n}y"] + dictionary[f"p{n}speedy"] 

    for n in range(2, dictionary["numberofplanets"] + 1):
        dictionary[f"p{n}x"] = dictionary[f"p{n}x"] + screenwidth/2 - dictionary["p1x"] #ändrar så att kameran är centrerad på planet 1
        dictionary[f"p{n}y"] = dictionary[f"p{n}y"] + screenheight/2 - dictionary["p1y"]

    pixelx = pixelx - dictionary["p1x"] #gör så att bakgrunden följer efter
    pixely = pixely - dictionary["p1y"]

    dictionary["p1x"] = screenwidth/2 #placerar planet 1 i mitten
    dictionary["p1y"] = screenheight/2

    # renderering



    clock.tick(60)  # 60 fps

pygame.quit()