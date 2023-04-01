from math import *

class vector():
    def __init__(self,x,y) -> None:
        self.x= x
        self.y= y
    def setx(self,value):
        self.x = value
    def getx(self):
        return self.x
    def sety(self,value):
        self.y = value
    def gety(self):
        return self.y
    def setangle(self,angle):
        length = vector.getlength(self)
        self.x = (cos(angle)*length)#+vector.getx(self)
        self.y = (sin(angle)*length)#+vector.gety(self)
    def getangle(self):
        return atan2(self.y,self.x)
    def setlength(self,length):
        angle = vector.getangle(self)
        self.x = (cos(angle)*length)#+vector.getx(self)
        self.y = (sin(angle)*length)#+vector.gety(self)
    def getlength(self):
        return sqrt(self.x**2+self.y**2)
    def add(self,v2):
        return vector(self.x+v2.getx(),self.y+v2.gety())
    def subtract(self,v2):
        return vector(self.x-v2.getx(),self.y-v2.gety())
    def multiply(self,val):
        return vector(self.x+val,self.y+val)
    def divide(self,val):
        return vector(self.x+val,self.y+val)
    def addto(self,v2):
        self.x += v2.getx()
        self.y += v2.gety()
    def subtractfrom(self,v2):
        self.x -= v2.getx()
        self.y -= v2.gety()
    def multiplyby(self,val):
        self.x *= val
        self.y *= val
    def divideby(self,val):
        self.x /= val
        self.y /= val