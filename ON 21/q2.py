class Picture:
    def __init__(self,Desc,Width,Height,FrameColour):
        self.__Description = Desc # String
        self.__Width = Width # Integer
        self.__Height = Height # Integer
        self.__FrameColour = FrameColour # String
    
    def GetDescription(self):
        return(self.__Description)
    def GetWidth(self):
        return(self.__Width)
    def GetHeight(self):
        return(self.__Height)
    def GetFrameColour(self):
        return(self.__FrameColour)
    def SetDescription(self, Description):
        self.__Description = Description
    

PictureArray = [Picture("",0,0,"") for i in range(100)]


def ReadData():
    try:
        count = 0
        file = open(r"C:\Users\Baldeep\Desktop\YR13CS\YR13\ON 21\Pictures.txt", "r")
        for i in range(len(PictureArray)):
            Description = file.readline()
            Width = file.readline()
            Height = file.readline()
            FrameColour = file.readline()
            PictureArray[i] = Picture(Description, Width, Height, FrameColour)
            count += 1
        print(PictureArray)
        print(count)
        file.close()
    except:
        print("File Not Found !")
    return count, PictureArray

ReadData()

    