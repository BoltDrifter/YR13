def init():
    global Array 
    Array = [0 for i in range(4)]
    TopPointer = 0
    EndPointer = -1
    NumberInQueue = 0
    for i in range(len(Array)):
        print(Array[i])
    
    return(TopPointer, EndPointer,NumberInQueue)

def AddItem(TopPointer, EndPointer, NumberInQueue):
    MaxQueue = len(Array)
    ask = input("Enter Data: ")
    if NumberInQueue < MaxQueue:
        EndPointer += 1
        if EndPointer > MaxQueue:
            EndPointer = 0
        Array[EndPointer] = ask
        NumberInQueue += 1
    else:
        print("Queue Full !")
    for i in range(len(Array)):
        print(Array[i])
    print(f"Top Pointer: {TopPointer}")
    print(f"End Pointer: {EndPointer}")
    return(TopPointer,EndPointer,NumberInQueue)

def RemoveItem(TopPointer, EndPointer, NumberInQueue):
    TopPointer = TopPointer + 1 
    print(f"Top Pointer: {TopPointer}")
    print(f"End Pointer: {EndPointer}")
    return(TopPointer, EndPointer,NumberInQueue)


def Print():
    pass


a,b,c = init()

AddItem(a,b,c)
m = a
s = b
f = c
Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
"""))
while Choice != 4:
    if Choice == 1:
        k,d,e = AddItem(m,s,f)
        m = k
        s = d
        f = e
        Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
"""))
    if Choice == 2:
       m,s,f = RemoveItem(m,s,f)
       Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
"""))
    if Choice == 3:
        Print()
    if Choice == 4:
        quit()
