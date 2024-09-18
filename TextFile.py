import pickle


class CarRecord: # declaring a class without other methods
    def __init__(self): # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00



ThisCar = CarRecord()

CarFile  = open('CarFile.DAT','rb+')
Address = hash(ThisCar.VehicleID)
CarFile.seek(Address)
pickle.dump(ThisCar,CarFile)

CarFile.close()

CarFile = open('CarFile.DAT','rb') # open file for binary read
Address = hash(ThisCar.VehicleID)
CarFile.seek(Address)
ThisCar = pickle.load(CarFile) # load record from file
CarFile.close()

print(ThisCar)