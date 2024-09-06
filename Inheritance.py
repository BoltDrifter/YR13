from calendar import week
import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

# other Get methods go here
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(week-3)
    def GetTitle(self):
        return(self.__Title)
    def GetAuthor(self):
        return(self.__Author__Artist)
    def GetID(self):
        return(self.__ItemID)
    def GetOnLoan(self):
        return(self.__OnLoan)
    def GetDueDate(self):
        return(self.__DueDate)    
    def Returning(self):
        self.__OnLoan = False
    def PrintDetails(self):
        print(self.__Title,',', self.__Author__Artist,',')
        print(self.__ItemID,",",self.__OnLoan,",",self.__DueDate)

class Books(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested = False
        self.__IsRequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested = True
class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self,g):
        self.__Genre = g
    
CDs = [0 for i in range(5)]
for i in range(len(CDs)):
    Title = input("Title: ")
    Author = input("Author: ")
    ID =  int(input("ID No: "))
    onLoan = input("OnLoan, True or False: ")
    CDs[i] = CD(Title, Author, ID)
    if onLoan == "True":
        CDs.Borrowing()
    elif onLoan == "False":
        CDs.Returning()

for i in range(len(CDs)):
    onL = CDs[i].GetOnLoan()
    if onL == False:
        print(CDs[i].GetID)

BooksArr = [0 for i in range(5)]
for i in range(len(CDs)):
    Title = input("Title: ")
    Author = input("Author: ")
    ID =  int(input("ID No: "))
    onLoan = input("OnLoan, True or False: ")
    BooksArr[i] = CD(Title, Author, ID)
    if onLoan == "True":
        BooksArr.Borrowing()
    elif onLoan == "False":
        BooksArr.Returning()

for i in range(len(BooksArr)):
    onL = BooksArr[i].GetOnLoan()
    if onL == False:
        print(BooksArr[i].GetID)