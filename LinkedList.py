NULLPOINTER = -1

class ListNode :
  def __init__(self) :
    self.Data = "-"
    self.Pointer = NULLPOINTER

# Initialize the Linked List

def InitialiseList() :
    List = [ListNode() for i in range(8)]
    StartPointer = NULLPOINTER 
    FreeListPtr = 0 
    for Index in range(7) : 
        List[Index].Pointer = Index + 1
        print("[",Index,"] ",List[Index].Data,"  ",List[Index].Pointer) 
    List[7].Pointer = NULLPOINTER 
    print("[",7,"] " ,List[7].Data,"  ",List[7].Pointer)
    return(List, StartPointer, FreeListPtr)

# Insertion of Data 

def InsertNode(List, StartPointer, FreeListPtr, NewItem) :
    s="a"
    if FreeListPtr != NULLPOINTER :
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        PreviousNodePtr = nullpointer
        ThisNode = Startpointer
        while ThisNode != nullpointer and List[ThisNode].Data < NewItem:
            PreviousNodePtr = List[ThisNode].Pointer
            ThisNode = List[ThisNode].Pointer
        if PreviousNodePtr == nullpointer:
            List[NewNodePtr].Pointer = Startpointer
            Startpointer = NewNodePtr
        else:
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
    else:
        print("No space for more data")
        s = "full"
        return(List,Startpointer,FreeListPtr,s)


a,b,c = InitialiseList()
print(a)
for x in range(len(a)):
    ask = int(input("Enter Data: "))
    insertnode(a, b, c, ask)
print(a)