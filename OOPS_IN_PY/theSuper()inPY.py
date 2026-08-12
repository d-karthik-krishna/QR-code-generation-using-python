class area:
    def __init__(self,shape):
        print(f"this is to find the area of a {shape}")
        
class Circle(area):
    def __init__(self, shape,radius):
        super().__init__(shape)
        print("Area = ",(3.14*radius*radius))

class Square(area):
    def __init__(self, shape,length):
        super().__init__(shape)
        print(f"Area = {length*length}")

class brbr:
    def __init__(self,shape):
        super().__init__(shape)
        
c = Circle("circle",4)  
s = Square("Square",4)