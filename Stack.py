array = [0 for x in range(10)]


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
    for i in range(len(array)):
       ask = int(input("Enter Data: "))
       array[i] = ask
       toppointer = i
       if basepointer == 0:
           basepointer = i
    print(array)
    print("Top Pointer: ",toppointer)
    print("Base Pointer: ",basepointer)

def delData(array,number):
    n_to_be_deleted = 0
    previous_index = 0
    for i in range(len(array)):
        if array[i] == number:
            n_to_be_deleted = i
            previous_index = i-1
        toppointer = previous_index
    print("Top Pointer: ",toppointer)


addData(array)
delData(array,20)
