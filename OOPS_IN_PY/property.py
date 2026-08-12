# property decorator in python hels in defining a method as a property, gives us getter and setter methods and even a delete method

class rectangle:
    def __init__(self,length, width):
        self._length = length #this means they are declared privately i.e _variable = they are declared as private
        self._width = width
    
    @property    
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def length(self):
        return f"{self._length:.1f}cm"
    
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self.width=new_width
        else:
            print("Width must be greater than 0")
            
    @width.setter
    def length(self,new_length):
        if new_length>0:
            self.length=new_length
        else:
            print("length must be greater than 0")
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
rect = rectangle(7,8)

rect.length=0
print(rect.width)

print(rect.length)
rect1 = rectangle(0,0)
print(rect1.length)

del rect.width