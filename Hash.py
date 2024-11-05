class Student:
    def __init__(self,Name,SchoolName,StudentID,DOB,YRGroup):
        self.__Name = Name
        self.__SchoolName = SchoolName
        self.__StudentID = StudentID
        self.__DOB = DOB
        self.__YRGroup = YRGroup
    def GetName(self):
        return self.__Name
    def GetSchoolName(self):
        return self.__SchoolName
    def GetStudentID(self):
        return (self.__StudentID)
    def GetDOB(self):
        return self.__DOB
    def GetYRGroup(self):
        return self.__YRGroup
    def SetName(self,Name):
        self.__Name = Name
    def SetSchoolName(self,SN):
        self.__SchoolName = SN
    def SetStudentID(self,ID):
        self.__StudentID = ID
    def SetDOB(self,DOB):
        self.__DOB = DOB
    def SetYRGroup(self,YG):
        self.__YRGroup = YG

StudArray = [Student("", "", 0, "", "") for i in range(2)]
HashTable = ["" for i in range(len(StudArray))]



def Hash(Key):
    s = StudArray[Key].GetStudentID()
    Index = s % 10
    print(Index)
    return Index

def Insert(Index):
    if Index == "" and Index < len(StudArray):
        HashTable[Index] = Student(Name, SchoolName,StudentID, DOB, YRGroup)
    else:
        Index = Index + 1

for i in range(len(StudArray)):
    Name = input("Enter Name: ")
    SchoolName = input("Enter School Name: ")
    StudentID = int(input("Enter ID: "))
    DOB = input("Enter DOB: ")
    YRGroup = int(input("Enter Year Group: "))
    StudArray[i] = Student(Name, SchoolName, StudentID, DOB, YRGroup)
a = Hash(i)
Insert(a)


