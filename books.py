# Create an object list for library items
#objects of 10 items
#Filter by on loan true

class Library:
    def __init__(self,e,d,f,g,j):
        self.__Title = e
        self.__Author = d
        self.__ItemId = f
        self.__OnLoan = g
        self.__DueDate = j
    def GetTitle(self):
        return(self.__Title)
    def GetAuthor(self):
        return(self.__Author)
    def GetID(self):
        return(self.__ItemId)
    def GetOnLoan(self):
        return(self.__OnLoan)
    def GetDueDate(self):
        return(self.__DueDate)
    def SetOnLoan(self,p):
        self.__OnLoan = p
    def PrintDetails(self):
        return(self.__Title,self.__Author,self.__ItemId,self.__OnLoan,self.__DueDate)


Libraryitems = [0 for i in range(10)]

for i in range(len(Libraryitems)):
    Title = input("Title: ")
    Author = input("Author: ")
    ID =  int(input("ID No: "))
    OnLoan = input("Choose true of False if on loan: ")
    DueDate = input("Due Date: ")
    Libraryitems[i] = Library(Title,Author,ID,OnLoan,DueDate)
for i in range(len(Libraryitems)):
    if Libraryitems[i].GetOnLoan() == "True":
        print(Libraryitems[i].GetTitle())

x = Libraryitems[0].PrintDetails()
print(x)