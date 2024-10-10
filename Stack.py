nullpointer = -1
class Node:
    def __init__(self):
        self.Data = "-"
        self.Pointer = nullpointer

def InitializeList():
    global List
    List = [Node() for i in range(8)]
    StartPointer = nullpointer
    FreeListPtr = 0 
    for Index in range(7) : 
        List[Index].Pointer = Index + 1
        print("[",Index,"] ", List[Index].Data,"  ",List[Index].Pointer) 
    List[7].Pointer = nullpointer 
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(List, StartPointer, FreeListPtr)

def Push(TopPointer, FreeListPointer):
    ask = input("Enter Data: ")
    Pre = FreeListPointer
    List[FreeListPointer].Data = ask
    TopPointer = TopPointer + 1 
    FreeListPointer += 1
    if List[FreeListPointer].Data == "-":
        List[TopPointer].Pointer = - 1
        List[TopPointer - 1].Pointer = Pre
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data}  {List[i].Pointer}")
    print(f"Top Pointer: {TopPointer}")
    print(f"Free Pointer: {FreeListPointer}")
    return(TopPointer,FreeListPointer)

def Pop(TopPointer,FreeListPtr):
    TopPointer = List[TopPointer].Pointer - 1
    FreeListPtr = FreeListPtr -  1 
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data}  {List[i].Pointer}")
    print(f"Top Pointer: {TopPointer}")
    print(f"Free Pointer: {FreeListPtr}")
    return(TopPointer, FreeListPtr)


def PrintArray():
    for i in range(len(List)):
        print(f"[{i}]   {List[i].Data}  {List[i].Pointer}") 
    

Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
"""))

a,b,c = InitializeList()
s = b
f = c  

while Choice != 4:
    Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
"""))
    if Choice == 1:
        d,e = Push(s,f)
        s = d
        f = e
    if Choice == 2:
       s,f = Pop(s,f)
       
    

# a,b,c = InitializeList()
# d,e = Push(b,c)
# f,g = Push(d,e)

for i in range(len(List)):
    d,e = Push()
# print(d)
# print(e)
# Pop(b,c)
# PrintArray()