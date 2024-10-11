def init():
    global Array 
    Array = ["-"for i in range(8)]
    TopPointer = 0
    EndPointer = -1
    NumberInQueue = 0
    print(" ")
    for i in range(len(Array)):
        print(f"[{i}]   {Array[i]}")
    return(TopPointer, EndPointer,NumberInQueue)

def AddItem(TopPointer, EndPointer, NumberInQueue):
    global MaxQueue
    MaxQueue = len(Array)
    ask = input("Enter Data: ")
    if NumberInQueue < MaxQueue:
        EndPointer += 1
        if EndPointer > MaxQueue:
            EndPointer = 0
        Array[EndPointer] = ask
        NumberInQueue += 1
    elif NumberInQueue >= MaxQueue:
        print("Queue Full !")
    print(NumberInQueue,MaxQueue)
    print("   ")
    for i in range(len(Array)):
        print(f"[{i}]   {Array[i]}")
    print("   ")
    print(f"Top Pointer: {TopPointer}")
    print(f"End Pointer: {EndPointer}")
    return(TopPointer,EndPointer,NumberInQueue)

def RemoveItem(TopPointer, EndPointer, NumberInQueue):
    if NumberInQueue == MaxQueue:
        TopPointer = TopPointer + 1 
        EndPointer = -1
        NumberInQueue = 0
    for i in range(len(Array)):
        print(f"[{i}]   {Array[i]}")
    return(TopPointer, EndPointer,NumberInQueue)


def Print():
    for i in range(len(Array)):
        print(f"[{i}]   {Array[i]}")



a,b,c = init()
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
    if Choice == 2:
       m,s,f = RemoveItem(m,s,f)
    if Choice == 3:
        Print()
    if Choice == 4:
        quit()
    Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
                           
"""))