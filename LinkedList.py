nullpointer = -1

class ListNode :
  def __init__(self) :
    self.Data = "-"
    self.Pointer = nullpointer

# Initialize the Linked List

def InitialiseList() :
    global List
    List = [ListNode() for i in range(8)]
    StartPointer = nullpointer
    FreeListPtr = 0 
    for Index in range(7) : 
        List[Index].Pointer = Index + 1
        print("[",Index,"] ",List[Index].Data,"  ",List[Index].Pointer) 
    List[7].Pointer = nullpointer
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(StartPointer, FreeListPtr)

# Insertion of Data 

def InsertNode(Startpointer, FreeListPtr) :
    ask = int(input("Enter Data: "))
    if FreeListPtr != nullpointer :
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = ask
        FreeListPtr = List[FreeListPtr].Pointer
        PreviousNodePtr = nullpointer
        ThisNode = Startpointer
        while ThisNode != nullpointer and List[ThisNode].Data < ask:
            PreviousNodePtr = List[ThisNode].Pointer
            ThisNode = List[ThisNode].Pointer
        if PreviousNodePtr == nullpointer:
            List[NewNodePtr].Pointer = Startpointer
            Startpointer = NewNodePtr
        else:
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
        if List[FreeListPtr].Data == "-":
            List[PreviousNodePtr].Pointer = -1
    else:
        print("No space for more data")
    for Index in range(7) : 
        List[Index].Pointer = Index + 1
        print("[",Index,"] ",List[Index].Data,"  ",List[Index].Pointer) 
    List[7].Pointer = nullpointer
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(Startpointer,FreeListPtr)
    
def deleteNode(Startpointer,FreeListPtr):
    Pre = List[Startpointer - 1].Pointer 
    FreeListPtr = FreeListPtr - 1
    List[Startpointer].Pointer = Pre
    print(Startpointer, FreeListPtr)
    return(Startpointer,FreeListPtr)

a,b = InitialiseList()

m = a
s = b

Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
                   
"""))
while Choice != 4:
    if Choice == 1:
        c,d = InsertNode(m,s)
        m = c
        s = d
    if Choice == 2:
       m,s= deleteNode(m,s)
    if Choice == 3:
        # Print()
        pass
    if Choice == 4:
        quit()
    Choice = int(input("""
1. Push
2. Pop
3. Output
4. End
                           
"""))