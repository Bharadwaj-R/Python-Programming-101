class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):  #this function is called whenever print() is called.
        '''By default, it prints the object type, but if it is customised,
then it will print the returned value instead of the object type, when print
is called'''
        return '({0},{1})'.format(self.x,self.y)
    

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)

p1=Point(1,2)
p2=Point(3,4)
print(p1+p2)
