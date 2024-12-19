class TreasureChest:
    def __init__(self,ques,ans,points):
        self.__question = ques
        self.__answer = ans
        self.__points = points
    def GetQuestion(self):
        return self.__question
    def CheckAnswer(self,answerP):
        if int(self.__answer) == answerP:
            return True
        else:
            return False 
    def getPoints(self,Attempts):
        if Attempts == 1: 
            return self.__points
        elif Attempts == 2:
            return (self.__points / 2)
        elif Attempts == 3 or Attempts == 4:
            return (self.__points / 4)  
        else:
            return 0


def readData():
    global arrayTreasure
    try:
        file = open(r"06_9618_41_Confidential Source Files June 2021\TreasureChestData.txt","r")
        arrayTreasure = []
        for i in range(0,5):
            question = file.readline().strip()
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure[i] = TreasureChest(question,answer,points)
    except:
        print("File Not Found!")


readData()

QNo = int(input("Enter Question Number: "))
Attempts = 1
Question = arrayTreasure[QNo].GetQuestion()
Answer = input("Enter Answer: ")
Check = arrayTreasure[QNo].CheckAnswer(Answer)
while Check == False:
    print("Wrong Answer: ")
    Answer = input("Enter Answer: ")
    Attempts += 1
Points = arrayTreasure[QNo].getPoints(Attempts)
print(Points)