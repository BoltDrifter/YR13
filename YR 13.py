# choice = "" 
# while choice !="A" and choice !="B" and choice !="C" and choice !="D" and choice !="E" and choice !="F" and choice !="U" :
#     choice = input("Enter your Grade: ")
#     if choice == "A": 
#         print("You Have achicved the top grade!") 
#         quit()
#     elif choice == "F" or choice == "U":
#         print("You have failed the exam") 
#         quit() 
#     elif choice == "B" or choice == "C" or choice == "D" or choice == "E":
#         print("You have passed the exam")
#         quit()
#
# choice = int(input("""If you want to:
#
# Add: press 1
# Sub : press 2
# Multiply : press 3
# Divide : press 4
# Square : press 5
# Mod : press 6
# Integer Division : press 7
#
# """))
#
# if choice == 1:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 + num2)
# if choice == 2:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 - num2)
# if choice == 3:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 * num2)
# if choice == 4:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 / num2)
# if choice == 5:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1**num2)
# if choice == 6:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 % num2)
# if choice == 7:
#   num1 = int(input("Enter a number: "))
#   num2 = int(input("Enter another number: "))
#   print(num1 // num2)
#
#
# choice = int(input("Enter a number between 1 to 10: "))

# if choice > 0 and choice < 11:
#   print("Correct Input !")

# while choice < 1 or choice > 10:
#   print("Invalid choice")
#   choice = int(input("Enter a number between 1 to 10: "))
#   if choice > 0 and choice < 11:
#     print("Correct Input !")
#     quit()


# Mark = []
# for x in range(1,5):
#     y = input("Food Name: ")
#     Mark.append(y)
# print(Mark)

# choice = int(input("Which Food do you want to change: "))

# while choice > len(Mark):
#     choice = int(input("Which Food do you want to change: "))

# Mark[choice] = input("Food Name: ")

# print(Mark)

# twoD = [[],
#         [],
#         [],
#         []]
# num = int(input("How many numbers per list in the 2D array: "))
# for x in range(len(twoD)):
#     for j in range(0, num):
#         y = input("Data Value to be stored in 2D Array: ")
#         twoD[x].append(y)
# print(twoD)


# A = {2,54,34,32,4}
# B = {3,54,43,3,23,432,34} 
# print(A | B)
# print(A & B)

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

Car1 = Car("TO84304",343143)
Car2 = Car("OPIRE21981", 3708370)

choice = int(input("Price: "))

Car1.SetPurchasePrice(choice)
Car1.SetDate("12/4/12")

Car2.SetDate("9/12/24")

y = Car2.GetDate()
x = Car1.GetPrice()

print(f"The Price is: {x}")
print(f"The date of registration is: {y}")






