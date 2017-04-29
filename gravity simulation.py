from physics import *
import pygame
import time,random



class particle(physics):
    def __init__(self,pos,_type_,size):
        super(particle,self).__init__()
        # type of the particles
        # type->1 | dynamic
        # type->2 | static
        self._type_ = _type_
        # size of the particle    
        self.radius = size
        self.pos.assign(pos[0],pos[1],pos[2])
    def random(self):
        self.radius = random.uniform(1,5)
        self.pos.x,self.pos.y,self.pos.z = random.uniform(0,window[0]),random.uniform(0,window[1]),0
        self._type_ = '1'
        self.mass = random.uniform(10e10,10e11)
    def get(self):
        return self.pos,self.radius
    def update(self):
        if self._type_ == '1':
           self.updatePos()



def _input_():
    global particles
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            p = pygame.mouse.get_pos()
##            p1 = particle((p[0],p[1],0),'1',5)
##            p1.mass = 10e10
            #particles.append(p1)
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
def allocateParticles():
    global window,particles
    for i in range(0,100):
        p = particle((0,0,0),'1',1)
        p.random()
        particles.append(p)



def applyForces():
    global particles,G
    for p in particles:
        for k in particles:
            
            mag = (G*k.mass*p.mass)/((dist(k.pos,p.pos)**2)+0.01)
            # print mag
            dir_ = vector((0,0,0),(0,0,0))
            
            dir_.assign(p.pos.get(),k.pos.get())
            
            p.applyForce2(mag,dir_)
       #print '\nforce',p.force.get(),p.force.mag
       #print '\nAcc',p.acc.get(),p.acc.mag
        
def textShow(_str_,qty,pos):
    
    font = pygame.font.SysFont("calibri",20)
    pop = font.render(_str_+" : "+str(qty),True,WHITE)
    screen.blit(pop,pos)
def drawArrow(pos,vctr):
    vctr.normalized()
    vctr.mult(50)
    pos1 = (int(pos.x),int(pos.y))
    pos2 = (pos1[0]+int(vctr.x/10e10),pos1[1]+int(vctr.y/10e10))
    #print pos1,pos2
    pygame.draw.line(screen,BLUE,pos1,pos2,int(2))
##    pygame.draw.line(screen,BLUE,pos2,(pos2[0]-5,pos2[1]-5),int(2))
##    pygame.draw.line(screen,BLUE,pos2,(pos2[0]-5,pos2[1]+5),int(2))
def gameLogic():
    global particles,G
    for j in range(0,len(particles)):
        for i in range(1+j,len(particles)):
            #if particles[j].pos
            if isInsideCir(particles[j].pos,particles[j].radius,particles[i].pos,particles[i].radius):
              if particles[i].radius < particles[j].radius:
                  particles[j].mass+= particles[i].mass
                  particles[j].radius+= particles[i].radius
                  
                  particles.remove(particles[i])
                  break
              else:
                  particles[i].mass+= particles[j].mass
                  particles[i].radius+= particles[j].radius
                  particles.remove(particles[j])
                  break
def normalizeCords(p):
    
    global particles
    flag = 0
    for p in particles:
        if p.radius > 15:
            flag = 1
    if flag ==1 or p == 1:
        for p in particles:
            p.radius /= 1.5

def display(prt):
    global screen
    for p in prt:
        
        pygame.draw.circle(screen,BLUE,(int(p.pos.x),int(p.pos.y)),int(p.radius))
        
def timeline():
    global particles,window
    for p in particles:
        p.update()
        p.bound2d_swap(window)
        p.velocity.divide(5)
        drawArrow(p.pos,p.force)
def main():
    global particles,window
    allocateParticles()
    applyForces()
    for p in particles:
        p.assign_dt(0.0015)
    normalizeCords(1)
    normalizeCords(1)
    while True:
         # setting the smallest time variation
         clock.tick(60)
         # Fill the background color to screen as black
         screen.fill(BLACK) 
         _input_()
         applyForces()
         gameLogic()
         display(particles)
         normalizeCords(0)
         
         textShow('particles :',len(particles),(10,10))
##          
         timeline()
         pygame.display.update()
         

         

# ======================
# initilising the pygame
# ======================

# colors 
WHITE = (254,254,254)
RED = (254,0,0)
BLACK = (0,0,0)
BLUE = (0,0,254)
YELLOW = (254,254,0)

# init the pygame 
window = (900,600)
pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()

# global variables
particles = list()

v = vector((0,10,0),(500,250,0))

# main function
main()
