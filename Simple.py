choice = "" 
while choice !="A" and choice !="B" and choice !="C" and choice !="D" and choice !="E" and choice !="F" and choice !="U" :
    choice = input("Enter your Grade: ")
    if choice == "A": 
        print("You Have achicved the top grade!") 
        quit()
    elif choice == "F" or choice == "U":
        print("You have failed the exam") 
        quit() 
    elif choice == "B" or choice == "C" or choice == "D" or choice == "E":
        print("You have passed the exam")
        quit()

choice = int(input("""If you want to:

Add: press 1
Sub : press 2
Multiply : press 3
Divide : press 4
Square : press 5
Mod : press 6
Integer Division : press 7

"""))

if choice == 1:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 + num2)
if choice == 2:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 - num2)
if choice == 3:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 * num2)
if choice == 4:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 / num2)
if choice == 5:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1**num2)
if choice == 6:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 % num2)
if choice == 7:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(num1 // num2)


choice = int(input("Enter a number between 1 to 10: "))

if choice > 0 and choice < 11:
  print("Correct Input !")

while choice < 1 or choice > 10:
  print("Invalid choice")
  choice = int(input("Enter a number between 1 to 10: "))
  if choice > 0 and choice < 11:
    print("Correct Input !")
    quit()


Mark = []
for x in range(1,5):
    y = input("Food Name: ")
    Mark.append(y)
print(Mark)

choice = int(input("Which Food do you want to change: "))

while choice > len(Mark):
    choice = int(input("Which Food do you want to change: "))

Mark[choice] = input("Food Name: ")

print(Mark)

twoD = [[],
        [],
        [],
        []]
num = int(input("How many numbers per list in the 2D array: "))
for x in range(len(twoD)):
    for j in range(0, num):
        y = input("Data Value to be stored in 2D Array: ")
        twoD[x].append(y)
print(twoD)


A = {2,54,34,32,4}
B = {3,54,43,3,23,432,34} 
print(A | B)
print(A & B)
