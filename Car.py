class Car:

    def __init__(self,n,e):
        self.__vehicleID =  n
        self.__Registration =  ""
        self.__DateofRegistration = None 
        self.__EngineSize =  e
        self.__PurchasePrice = 0.00
    def SetPurchasePrice(self,p):
        self.__PurchasePrice = p
    def SetRegistration(self, r):
        self.__Registration = r
    def SetDate(self,d):
        self.__DateofRegistration = d
    def GetID(self):
        return(self.__vehicleID)
    def GetRegis(self):
        return(self.__Registration)
    def GetDate(self):
        return(self.__DateofRegistration)
    def GetSize(self):
        return(self.__EngineSize)
    def GetPrice(self):
        return(self.__PurchasePrice) 

CarArray = [0 for i in range(10)]
for i in range(len(CarArray)):
    vehID = input("Enter Vehicle Id: ")
    enginesize = int(input("Enter the engine side: "))
    CarArray[i] = Car(vehID,enginesize)
print(f"The Vehicle ID is ; {CarArray[1].GetID()}") 

high = 0 
id = None
for i in range(len(CarArray)):
    x = CarArray[i].GetSize()
    if high < x:
        high = x
        id = CarArray[i].GetID()
print(f"The Highest Engine Size is with: {id}")



# Car1 = Car("TO84304",343143)
# Car2 = Car("OPIRE21981", 3708370)
# Car3 = Car("OPIu41", 3708370)

# choice1 = int(input("Price: "))
# choice2 = int(input("Price: "))
# choice3 = int(input("Price: "))

# Car1.SetPurchasePrice(choice1)
# Car1.SetDate("12/4/12")

# Car2.SetDate("9/12/24")
# Car2.SetPurchasePrice(choice2)
# Car3.SetPurchasePrice(choice3)

# z = Car3.GetPrice()
# y = Car2.GetPrice()
# x = Car1.GetPrice()

# print(f"The Price is: {x}")
# print(f"The date of registration is: {y}")

# high = 0 

# if x > high:
#     high = x
# if z > high:
#     high = z
# if y > high:
#     high = y

# if high == z:
#     print(Car3.GetID())
# if high == x:
#     print(Car1.GetID())
# if high == y:
#     print(Car2.GetID())