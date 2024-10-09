array = [0 for x in range(4)]

# array2 = [34,65,4,3]

# - 1
# - 2 
# - 3 
# - 4
# - 5 
# - 6
# - 7
# - 8
# - 9
# - 10


def addData(array):
    basepointer = 0
    global toppointer  
    for i in range(0,len(array)):
       ask = int(input("Enter Data: "))
       array[i] = ask
       toppointer = i
       if basepointer == 0:
           basepointer = 0
    for x in range(len(array)):
        leng = len(array)
        # print(leng - x)
        print(array[leng-x-1])
    print("Top Pointer: ",toppointer)
    print("Base Pointer: ",basepointer)

def delData(array,number):
    previous_index = 0
    for i in range(len(array)):
        if array[i] == number:
            previous_index = i-1
        toppointer = previous_index
    print("Top Pointer: ",toppointer)
    





addData(array)
delData(array,43)
