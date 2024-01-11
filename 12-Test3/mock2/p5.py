'''
Class C describes a point (x,y) in the plane. The point coordinates are given when creating (initializing) the object. 
The class contains the m1() method that returns the number of the quadrant of the 
Cartesian system in which the point (x,y) is located ( https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) ). 
The m1() method returns 0 if the point (x,y) is located on the X-axis or Y-axis. 
The class contains the m2(a,b) method that returns true when the point (x,y) is in the same quadrant of the 
Cartesian system as the point with coordinates a,b. Otherwise, the method returns false. 
The class contains the m3(a,b) method that returns true when the distance between points (x,y) and (a,b) is greater than 5. 
Otherwise, the method returns false. Example:
p = C(2,3)
p.m1()  1
p.m2(7,4)  True
p.m2(-3,1)  False
p.m3(8,5)  True
p.m3(4,7)  False
p1 = C(0,5)
p1.m1()  0
p1.m2(4,7)  False
p1.m2(-7,0)  True
'''
class C():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
    def m2(self,a,b):
        if a>0 and b>0 and self.x>0 and self.y>0: # ćw.1
            return True
        if a<0 and b>0 and self.x<0 and self.y>0:
            return True
        if a<0 and b<0 and self.x<0 and self.y<0:
            return True
        if a>0 and b<0 and self.x>0 and self.y<0:
            return True
        return False
    def m3(self,a,b):
        if ((self.x-a)**2+(self.y-b)**2)**0.5 >5:
            return True
        else:
            return False
    

p = C(2,3)
print(p.m1()) # 1
print(p.m2(7,4)) # True
print(p.m2(-3,1)) # False
print(p.m3(8,5)) # True
print(p.m3(4,7)) # False
p1 = C(0,5)
print(p1.m1()) # 0
print(p1.m2(4,7)) # False
print(p1.m2(-7,0)) # True