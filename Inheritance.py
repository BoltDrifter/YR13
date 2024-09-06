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
    def GetBorrowing(self):
        print(self.__OnLoan)
    def SetBorrowing(self):
        self.__OnLoan = True
    def SetReturning(self):
        self.__OnLoan = False
class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre = ""
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self,g):
        self.__Genre = g
    def GetBorrowing(self):
        print(self.__OnLoan)
    def SetBorrowing(self):
        self.__OnLoan = True
    def SetReturning(self):
        self.__OnLoan = False
    
CDs = [0 for x in range(5)]
for x in range(len(CDs)):
    Title = input("Title: ")
    Author = input("Author: ")
    ID =  int(input("ID No: "))
    onLoan = input("OnLoan, True or False: ")
    CDs[x] = CD(Title, Author, ID)
    if onLoan == "True":
        CDs[x].SetBorrowing()
    elif onLoan == "False":
        CDs[x].SetReturning()

for i in range(len(CDs)):
    onL = CDs[x].GetOnLoan()
    if onL == False:
        print(CDs[x].GetID)

BooksArr = [0 for i in range(5)]
for i in range(len(CDs)):
    Title = input("Title: ")
    Author = input("Author: ")
    ID =  int(input("ID No: "))
    onLoan = input("OnLoan, True or False: ")
    BooksArr[i] = Books(Title, Author, ID)
    if onLoan == "True":
        BooksArr[i].SetBorrowing()
    elif onLoan == "False":
        BooksArr[i].SetReturning()


for i in range(len(BooksArr)):
    onL = BooksArr[i].GetOnLoan()
    if onL == False:
        print(BooksArr[i].GetID)