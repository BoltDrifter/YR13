arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearsearch(Data):
    for i in range(len(arrayData)):
        if arrayData[i] == Data:
            return True
        else:
            return False
        
ask = int(input("Enter Search Value: "))

x = linearsearch(ask)
if x == True:
    print("The Search Value was found!")
else: 
    print("The Search value was not found!")

def BubbleSort():
    temp = 0
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

BubbleSort()
print(arrayData)