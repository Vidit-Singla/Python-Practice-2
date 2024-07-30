class Shapes():
     def __init__(self):
          pass

class Square(Shapes):
    def __init__(self,length):
        self.length= length

    def Area(self):
         return self.length**2
    
s1= Square(4)
print(s1.Area())

