Array = [62,31,11,34,66,32]
MaxIndex = 6
n = MaxIndex - 1 
NoMoreSwaps = False

while NoMoreSwaps == False:
    NoMoreSwaps == True
    for j in range(n):
        if Array[j] > Array[j+1]:
            Temp = Array[j]
            Array[j] = Array[j+1]
            Array[j+1] = Temp
            NoMoreSwaps = False
    n = n - 1
for i in range(len(Array)):
    print(Array[i])