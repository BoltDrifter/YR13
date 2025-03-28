class vehicle:
    def __init__(self,i,s,a):
        self.__ID = i # String 
        self.__MaxSpeed = s # Integer
        self.__CurrentSpeed = 0 # Integer
        self.__IncreaseAmount = a # Integer
        self.__HorizontalPosition = 0 # Integer
    def GetCurrentSpeed(self):
        return(self.__CurrentSpeed)
    def GetIncreaseAmount(self):
        return(self.__IncreaseAmount)
    def GetHorizontalPosition(self):
        return(self.__HorizontalPosition)
    def GetMaxSpeed(self):
        return(self.__MaxSpeed)
    def SetCurrentSpeed(self,s):
        self.__CurrentSpeed = s
    def SetHorizontalPosition(self,h):
        self.__HorizontalPosition = h
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if(self.__CurrentSpeed > self.__MaxSpeed):
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__CurrentSpeed
    def Output(self):
        print(f"The Horizontal Position of the Vehicle is: {self.__HorizontalPosition} ")
        print(f"The Current Speed of the Vehicle is: {self.__CurrentSpeed} ")
class Helicopter(vehicle):
    def __init__(self, i, s , a, v ,h):
        vehicle.__init__(self,i,s,a)
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = a
        self.__HorizontalPosition = 0 
        self.__verticalPosition = 0 # Integer
        self.__verticalchange = v # Integer
        self.__MaxHeight = h # Integer
    def IncreaseSpeed(self):
        # vehicle.IncreaseSpeed(self)
        self.__verticalPosition = self.__verticalPosition + self.__verticalchange
        if (self.__verticalPosition < self.__MaxHeight) and (self.GetCurrentSpeed() < self.GetMaxSpeed()):
            self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
            self.__verticalPosition = self.__verticalPosition + self.__verticalchange
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
    def Output(self):
        # vehicle.Output(self)
        print(f"The Horizontal Position of the Vehicle is: {self.__HorizontalPosition} ")
        print(f"The Current Speed of the Vehicle is: {self.__CurrentSpeed} ")
        print(f"The Vertical Postition of helicopter: {self.__verticalPosition}")

Car = vehicle("Tiger", 100, 20)
Helicopters = Helicopter("Lion", 350, 40, 3 ,100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.Output()

Helicopters.IncreaseSpeed()
Helicopters.IncreaseSpeed()
Helicopters.Output()

#s23 p41