from physics import *
import pygame
import time,random,math





def draw():
    pass

i = vertex(10,-10,0)
f = vertex(0,5,0)

v = vector(i,f)
print v.get()
v.assign((0,0,5),(10,2,-4))
print v.get()

print v.magCal()
v.normalized()
print v.magCal()

'''
==========================================
    colors class
==========================================
'''  
class colors(object):
    def __init__(self):
        self.WHITE = (254,254,254)
        self.BLACK = (0,0,0)
        self.RED = (254,0,0,6)
        self.BLUE = (0,0,254)
        self.GREEN = (0,254,0)
        self.GRAY = (100,100,100)
        self.YELLOW = (254,254,0)
        self.MAGENTA = (254,0,254)


class mesh(physics):
    def __init__(self,pos):
        super(mesh,self).__init__()
        self.radius = 0.0
        self.pos.assign(pos[0],pos[1],pos[2])
    def randomize(self,window):
        self.pos.x = random.uniform(0,window[0])
        self.pos.y = random.uniform(0,window[1])
        self.pos.z = random.uniform(0,20)
        self.radius = random.uniform(0,20)
    def show():
        pass








def input():
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_LEFT:
                pass
        
'''
===============================================================================
===============================================================================
'''
# initilize the pygame
pygame.init()
# screen height and width
window = [600,400]
# center of the screen | environment cooords
cx,cy,cz = window[0]/2,window[1]/2, -5
# loading the icon  
# pygame.display.set_icon(pygame.image.load('Icon.png'))
# init the name of the window
pygame.display.set_caption("Gravity simulation - 2017")

# initilize the screen
screen = pygame.display.set_mode(window)
# initilize the clock
clock = pygame.time.Clock()


m1 = mesh((0,10,30))
gameOver = False
color = colors()

while True:
    # setting the smallest time variation
    dt = float(clock.tick(60))/1000
    clock.tick(60)
    # Fill the background color to screen as black
    screen.fill(color.WHITE)
    # input
    input()
    
    # update the screen
    pygame.display.update()
    # clear the screen
    screen.fill(color.WHITE)

    if gameOver == True :
        break















