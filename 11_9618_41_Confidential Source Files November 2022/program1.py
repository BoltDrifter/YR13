DataArray = [0 for i in range(0,100)]

def ReadFile():
    try:
        file = open(r"11_9618_41_Confidential Source Files November 2022\IntegerData.txt","r")
        for i in range(0,100):
            x = file.readline().strip()
            DataArray[i] = x
    except:
        print("File Not Found!")

def FindValues(Number):
    count = 0
    while Number < 1 or Number > 100:
        Number = int(input("Enter Number: ")) 
    for i in range(len(DataArray)):
        if Number == int(DataArray[i]):
            count = count + 1
    print(f"The number was found {count} times")
ReadFile()
FindValues(61)

def BubbleSort():
    global DataArray

    n = 100
    for i in range(n - 1):
        for j in range(n-i-1):
            if int(DataArray[j]) > int(DataArray[j+1]):
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp

BubbleSort()
print(DataArray)
