class Fruits:
    def __init__(self,name,colour,taste):
        self.name=name
        self.colour=colour
        self.taste=taste
    def ask(self):
        self.choice=input('what fruit do you like')
        print('so you like',self.choice,'interesting')
    def put(self):
        print('your input:',self.name,self.colour,self.taste)
        

fruit1=Fruits('mango','green','sour')
fruit2=Fruits('apple','red','crisp')
fruit1.put()
fruit2.put()
fruit1.ask()
