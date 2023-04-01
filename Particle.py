from Vector import *
from random import *
class particle():
    rad = pi/180

    def __init__(self,x,y,speed,direction,grav=0) -> None:
        self.x= x
        self.y= y
        self.speed= speed
        self.direction= direction
        self.position = vector(x,y)
        self.velocity = vector(0,0)
        self.velocity.setlength(speed)
        self.velocity.setangle(direction)
        self.gravity = vector(0,grav)
        self.mass =1
        self.radius =0
        self.bounce = -1
        self.friction = 1

    def acclerate(self,acc):
        self.velocity.addto(acc)
    
    def update(self):
        self.velocity.multiplyby(self.friction)
        self.velocity.addto(self.gravity)
        self.position.addto(self.velocity)
    def angleto(self,p2):
        return atan2(p2.position.gety() - self.position.gety(),p2.position.getx() - self.position.getx())

    def distanceto(self,p2):
        dx =p2.position.getx() - self.position.getx()
        dy =p2.position.gety() - self.position.gety()

        return sqrt(dx**2+dy**2)

    def gravityto(self,p2):
        grav = vector(0,0)
        dist =  self.distanceto(p2)

        grav.setlength(p2.mass/(dist**2))
        grav.setangle(self.angleto(p2))
        self.velocity.addto(grav)

        

