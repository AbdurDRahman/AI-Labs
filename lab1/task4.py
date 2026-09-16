import math 

class MyVector:
    def __init__(self , x = 0.0 , y = 0.0) -> None:
        self.x = x 
        self.y = y
        return  
    def update_x(self , x:float) -> None:
        self.x = x 
        return 
    def update_y(self , y:float) -> None:
        self.y = y 
        return 
    def magnitude(self) -> float :
        return math.sqrt(self.x**2 + self.y**2)
    def direction(self) -> float : 
        return math.atan2(self.y , self.x)
    


test_vector = MyVector(5.0 , 3.0)
print(test_vector.magnitude())
print(test_vector.direction())