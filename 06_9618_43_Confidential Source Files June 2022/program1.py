PlayerName = ["" for i in range(0,11)]
PlayerScores = [0 for i in range(0,11)]

def ReadingHighScores():
    file = open(r"06_9618_43_Confidential Source Files June 2022\HighScore.txt","r")
    for i in range(0,10):
        x = file.readline().strip()
        y = file.readline().strip()
        PlayerName[i] = x
        PlayerScores[i] =  y
def OutputHighScores():
    print("PlayerName Score")
    print("")
    for i in range(0,10):
        print(f"{PlayerName[i]} {int(PlayerScores[i])}")

Name = input("Enter Three Chartacter Name: ")
while len(Name) != 3:
    Name = input("Enter Three Chartacter Name: ")
    Score = int(input("Enter Score:"))
while Score < 1 or Score > 100000:
    Score = int(input("Enter Score:"))

def NewList(Name, Score):
    NewPlayerArray =["" for i in range(0,11)]
    NewScoreArray = [0 for i in range(0,11)]
    for i in range(0,10):
        NewPlayerArray[i] = PlayerName[i].strip()
        NewScoreArray[i] = int(PlayerName[i])
        while len(Name) != 3:
            Name = input("Enter Three Chartacter Name: ")
        while Score < 1 or Score > 100000:
            Score = int(input("Enter Score:"))
        NewPlayerArray[10] = Name
        NewScoreArray[10] = Score
    print("PlayerName Score")
    print("")
    for i in range(len(NewPlayerArray)):
        print(f"{NewPlayerArray[i]} {NewScoreArray[i]}")

ReadingHighScores()
OutputHighScores()