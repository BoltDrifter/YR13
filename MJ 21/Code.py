class TreasureChests:
    def __init__(self, Question, Answer, Points):
        self.__question = Question # String
        self.__answer = Answer # Integer
        self.__points = Points # Integer 

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, Answer):
        if self.__answer == Answer:
            return True
        else:
            return False

    def getPoints(self, Attempts):
        if Attempts == 1:
            return self.__points
        if Attempts == 2:
            point = self.__points / 2
            return int(point)
        if Attempts == 3 or Attempts == 4:
            point = self.__points / 4
            return int(point)
        else: 
            return 0
            

# Q = TreasureChests("100/10", 10, 20)
# answer = int(input("ANswer: "))
# print(Q.checkAnswer(answer))
# attempts = 1

arrayTreasure = ["" for x in range(5)]

def readData():
    try:
        File = open(r"C:\Users\Baldeep\Desktop\YR13CS\YR13\MJ 21\TreasureChestData.txt", "r")
        for x in range(1,6):
            Question = File.readline()
            Answer = File.readline()
            Points = File.readline()
            arrayTreasure[x] = TreasureChests(Question,Answer,Points)
    except:
        print("File Not Found!")

readData()
QNo = int(input("Enter a question number , 1 to 5: "))
Question = arrayTreasure[QNo].getQuestion()
print(Question)
Answer = int(input("Enter your Answer: "))
check = arrayTreasure[QNo].checkAnswer(Answer)
print(check)
attempts = 0

# if check == False:
#     print(Question)
#     Answer = int(input("Enter your Answer: "))
#     attempts = attempts + 1
#     print(attempts)
if check == True:
    pointsawarded = arrayTreasure[QNo].getPoints(attempts) 
    print(pointsawarded)
