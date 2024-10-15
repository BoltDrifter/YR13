nullpointer = -1 

class Node:
    def __init__(self):
        self.Data = "-"
        self.Pointer = nullpointer

def InitializeList():
    global List 
    StartPointer = 0
    FreeListPtr = -1
    NumberinQueue = 0
    List = [Node() for i in range(8)]
    for index in range(len(List)):
        List[index].Pointer = index + 1
        print(f"[{index}]  {List[index].Data} {List[index].Pointer}")
    List[7].Pointer = nullpointer
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(List, StartPointer, FreeListPtr,NumberinQueue)

def Push(StartPointer, FreeListPtr,NumberInQueue):
    global MaxQueue 
    MaxQueue = len(List)
    Pre = FreeListPtr
    ask = int(input("Enter Data: "))
    if NumberInQueue < MaxQueue:
        FreeListPtr += 1
        if FreeListPtr > MaxQueue:
            FreeListPtr = 0
        List[FreeListPtr].Data = ask
        NumberInQueue += 1
    if List[FreeListPtr + 1].Data == "-":
        List[FreeListPtr].Pointer = -1
        List[FreeListPtr - 1].Pointer = Pre
    elif NumberInQueue >= MaxQueue:
        print("Queue Full !")
    print(NumberInQueue,MaxQueue)
    print("   ")
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data} {List[i].Pointer}")
    print("   ")
    print(f"Top Pointer: {StartPointer}")
    print(f"End Pointer: {FreeListPtr}")
    return(StartPointer,FreeListPtr,NumberInQueue)






a,b,c,d = InitializeList()

f,g,h = Push(b,c,d)
Push(f,g,h) 