import math
import pygame

p1y = float(200)
p1x = float(400)
# p1dir = float(90) # angle 0 being up 
p1speedx = float(4)
p1speedy = float(0)
p1mass = int(10000000)
f1 = int()

# sin x cos y

KonstG = 6.674*float(10**-11)
dist = float()
ang1 = float()
ang2 = float()

p2y = float(400)
p2x = float(400)
# p2dir = float(270)
p2speedx = float(-4.5)
p2speedy = float(0)
p2mass = int(10000000)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    pygame.draw.circle(screen, "red", (p1x, p1y), 30)
    pygame.draw.circle(screen, "blue", (p2x, p2y), 30)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # calculations

    dist = math.hypot((p1x-p2x),(p1y-p2y))
    ang1 = math.atan2((p2y-p1y),(p2x-p1x))
    f1 = (KonstG*p1mass*p2mass)/dist**2
    if dist <= 60:
        f1 *= -1
    p1speedx = p1speedx + math.cos(ang1)*f1
    p1speedy = p1speedy + math.sin(ang1)*f1
    p1x = p1x + p1speedx
    p1y = p1y + p1speedy

    ang2 = math.atan2((p1y-p2y),(p1x-p2x))
    p2speedx = p2speedx + math.cos(ang2)*f1
    p2speedy = p2speedy + math.sin(ang2)*f1
    p2x = p2x + p2speedx
    p2y = p2y + p2speedy
    clock.tick(60)  # limits FPS to 60
print(dist)
print(f1)
print(math.degrees(ang1))
print(math.cos(ang1)*f1)
print(math.sin(ang1)*f1)
pygame.quit()