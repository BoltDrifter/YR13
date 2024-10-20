nullpointer = -1 

class Node:
    def __init__(self):
        self.Data = "-"
        self.Pointer = nullpointer

def InitializeList():
    global List 
    StartPointer = 0
    EndPointer = -1
    NumberinQueue = 0
    List = [Node() for i in range(8)]
    for index in range(len(List)-1):
        List[index].Pointer = index + 1
        print(f"[{index}]  {List[index].Data} {List[index].Pointer}")
    List[7].Pointer = nullpointer
    print(f"[7] {List[7].Data} {List[7].Pointer}")
    return(StartPointer, EndPointer,NumberinQueue)

def Push(StartPointer, EndPointer ,NumberInQueue):
    global MaxQueue 
    MaxQueue = len(List)
    Pre = EndPointer + 1
    ask = int(input("Enter Data: "))
    if NumberInQueue < MaxQueue:
        EndPointer += 1
        if EndPointer > MaxQueue:
            EndPointer = 0
        List[EndPointer].Data = ask
        NumberInQueue += 1
        if EndPointer < 7:
            if List[EndPointer + 1].Data == "-":
                List[EndPointer].Pointer = -1
                List[EndPointer - 1].Pointer = Pre
        else:
            print("Queue Full !")
    print(NumberInQueue,MaxQueue)
    print("   ")
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data} {List[i].Pointer}")
    print("   ")
    print(f"Top Pointer: {StartPointer}")
    print(f"End Pointer: {EndPointer}")
    return(StartPointer,EndPointer,NumberInQueue)


def Pop(StartPointer, EndPointer, NumberInQueue):
    if NumberInQueue == MaxQueue:
        StartPointer = StartPointer + 1
        List[EndPointer].Pointer = StartPointer
        if EndPointer > MaxQueue:
            EndPointer = -1
        print(EndPointer)
        EndPointer += 1
        NumberInQueue = MaxQueue - 1
    print("   ")
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data} {List[i].Pointer}")
    print("   ")
    print(f"Top Pointer: {StartPointer}")
    print(f"End Pointer: {EndPointer}")
    return(StartPointer,EndPointer,NumberInQueue)

def Print():
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data}  {List[i].Pointer}")

a,b,c = InitializeList()
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
        k,d,e = Push(m,s,f)
        m = k 
        s = d
        f = e
    if Choice == 2:
       m,s,f = Pop(m,s,f)
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