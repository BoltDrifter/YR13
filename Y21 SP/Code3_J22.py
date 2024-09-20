class Card:
    def __init__(self,Number,Colour):
        self.__Number = Number #Integer  
        self.__Colour = Colour  #String
        self.__Selected = False # Boolean
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    def GetSelected(self):
        return self.__Selected
    def SetSelected(self):
        self.__Selected = True


Array = ["" for x in range(30)]

File = open("CardValues.txt","r")


try:
    for i in range(30):
        Number = File.readline()
        Colour = File.readline()
        Array[i] = Card(Number,Colour)
except:
    print("Not Working")
print(Array)

def ChooseCards():
    Index = int(input("Enter a number: "))
    while Index < 1 or Index > 30:
        Index = int(input("Enter a number: "))
    if Array[Index].GetSelected() == False:
        Array[Index].SetSelected()
        return Index
    while Array[Index].GetSelected() == True:
        Index = int(input("Already Chosen, Enter a number: "))
            

Player1 = ["" for i in range(4)]

for x in range(4):
    Cards = ChooseCards()
    N = Array[Cards].GetNumber()
    C = Array[Cards].GetColour()
    Player1[x] = Card(N,C)

print(Player1)
