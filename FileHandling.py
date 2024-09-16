import pickle

class CarRecord: # declaring a class without other methods
    def __init__(self): # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00




Car = [CarRecord() for x in range(100)]


CarFile = open('CarFile.DAT', 'wb')

for i in range(100):
    Car[i].VehicleID = input("Vehicle ID: ")
    Car[i].Registration = input("Registration No: ")
    Car[i].DateOfRegistration = input("Date: ")
    Car[i].EngineSize = int(input("Engine Size: "))
    Car[i].PurchasePrice = float(input("Price: "))
    pickle.dump(Car[i], CarFile)

CarFile.close()

CarFile = open('CarFile.DAT', 'rb')

Car = ["" for x in range(100)]

for i in range(100):
    Car[i] = pickle.load(CarFile)

CarFile.close()

print(Car)