StackVowels = ["" for i in range(0,100)]
StackConsonents = ["" for i in range(0,100)]

VowelTop = 0
ConsonentTop = 0

def PushData(Letter):
    if Letter == "a" or Letter == "e" or Letter == "i" or Letter == "o" or Letter == "u":
        if VowelTop == 100:
            print("Vowel stack full")
        else:
            StackVowels.append(Letter)
            VowelTop = VowelTop + 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack full")
        else:
            StackConsonents.append(Letter)
            ConsonantTop = ConsonantTop + 1

def ReadData():
    try:
        file = open("11_9618_42_SourceFiles\StackData.txt", "r")
        for i in range(0,100):
            x = file.readline().strip()
            PushData(x)
        file.close()
    except:
        print("File Not Found!")

def PopVowel():
    if StackVowels[VowelTop] == "":
        print("Stack is empty!")
    else:
        x = StackVowels[VowelTop]
        VowelTop =- 1
        return x

def PopConsonents():
    if StackConsonents[ConsonentTop] == "":
        print("Stack is empty!")
    else:
        x = StackConsonents[ConsonentTop]
        ConsonentTop =- 1
        return x
    


ReadData()
Letters = ""
Flag = False
for x in range(0, 5):
    Flag = False
    while Flag == False:
        Choice = input("Vowel or Consonant").lower()
        if Choice == "vowel":
            DataAccessed = PopVowel()
            if DataAccessed != "No data":
                Letters = Letters + DataAccessed
                Flag = True
            else:
                print("No vowels left")
        elif Choice == "consonant":
            DataAccessed = PopConsonents()
            if DataAccessed != "No data":
                Letters = Letters + DataAccessed
                Flag = True
            else:
                print("No consonants left")

print(Letters)