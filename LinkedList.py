nullpointer = -1

class ListNode:
    def __init__(self):
        self.Data = "-"
        self.Pointer = nullpointer
def InitialiseList():
    array = [ListNode() for i in range(8)]
    startpointer = nullpointer
    freelistptr = 0
    for index in range(7):
        array[index].pointer = index + 1
        print(f"[{index}] {array[index].Data} {array[index].pointer}")
    array[7].pointer = nullpointer
    print(f"[7] {array[index].Data} {array[7].pointer}")
    print(array)
    return(array, startpointer, freelistptr)

def insertnode(List,Startpointer, FreeListPtr, NewItem):
    s = "a"
    if FreeListPtr != nullpointer:
        NewNodePtr = FreeListPtr  
        List[FreeListPtr].Data = NewItem
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