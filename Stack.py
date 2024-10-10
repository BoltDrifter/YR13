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
        print("[",Index,"] ",List[Index].Data,"  ",List[Index].Pointer) 
    List[7].Pointer = nullpointer 
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(List, StartPointer, FreeListPtr)

def Push(Array, TopPointer, FreeListPointer):
    ask = input("Enter Data: ")
    Array[FreeListPointer] = ask
    TopPointer = List[TopPointer].Pointer + 1




a,b,c = InitializeList()
Push(a,b,c)
