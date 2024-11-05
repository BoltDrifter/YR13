def LinearSearch(array, Number):
    for x in range(len(array)):
        if array[x] == Number:
            return True
        else:
            return False

def bubbleSort():
   for x in range (0, 10):
      for y in range(0, 9):
         if theArray[y] < theArray[y + 1]:
            temp = theArray[y]
            theArray[y] = theArray[y + 1]
            theArray[y + 1] = temp


theArray = [10,5,6,7,1,12,13,15,21,8]

ask = int(input("Enter Value: "))

if LinearSearch(theArray,ask) == True: 
    print("Number Found !")
else:
    print("Number not found!")  
