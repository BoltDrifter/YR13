import pickle

class CarRecord: # declaring a class without other methods
    def __init__(self): # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00




Car = [CarRecord() for x in range(1000000)]

def Add():
    CarFile = open('CarFile.DAT', 'wb')

    for i in range(1):
        Car[i].VehicleID = int(input("Vehicle ID: "))
        Car[i].Registration = input("Registration No: ")
        Car[i].DateOfRegistration = input("Date: ")
        Car[i].EngineSize = int(input("Engine Size: "))
        Car[i].PurchasePrice = float(input("Price: "))
        pickle.dump(Car[i], CarFile)

    CarFile.close()



# Reading the Data

def Read():
    CarFile = open('CarFile.DAT', 'rb')
    i = int(input("Which Vehicle do you want data for, type the ID of the vehicle:  "))
    Address = hash(Car[i].VehicleID)
    CarFile.seek(Address)
    Data = pickle.load(CarFile)
    print(Data)

# Main Program 

choice = int(input("Enter How many records Do you want to add: "))
choice2  = int(input("Enter How many records you want to retrive: "))

for i in range(choice):
    Add()
for x in range(choice2):
    Read()