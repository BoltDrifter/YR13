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
        PreviousNodePtr = NULLPOINTER
        ThisNodePtr = StartPointer 
        while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data < NewItem:
            PreviousNodePtr = ThisNodePtr 
            ThisNodePtr = List[ThisNodePtr].Pointer
        if PreviousNodePtr == NULLPOINTER :
              List[NewNodePtr].Pointer = StartPointer
              StartPointer = NewNodePtr
        else : 
              List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
              List[PreviousNodePtr].Pointer = NewNodePtr
        print("This N P =",ThisNodePtr,"New N P =",NewNodePtr,"Pr N P =",PreviousNodePtr)
    else :
      print("No space for more data")
      s="full"
    
    return(List, StartPointer, FreeListPtr,s)
  
def Outputallnodes(List, StartPointer,FreeListPtr) :
    currentp=StartPointer
    while (currentp!=-1):
      print(List[currentp].Data, " ", List[currentp].Pointer)
      currentp=List[currentp].Pointer  
      
      
              
def GetOption() :
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output list")
    print("5: end program")
    option = input("Enter your choice: ")
    return(option)

Option = GetOption()
List, StartPointer, FreeListPtr = InitialiseList()
while Option != "5" :
  if Option == "1" :
      Data = input("Enter the value: ")
      List, StartPointer, FreeListPtr,s = InsertNode(List, StartPointer, FreeListPtr, Data)
      print("StartPointer ",StartPointer,", FreeListPtr ",FreeListPtr)
      for Index in range(len(List)) : 
        print("[",Index,"] ",List[Index].Data,"  ",List[Index].Pointer) 
      if s=="full":
        Option = GetOption()
  if Option=="4":
    Outputallnodes(List, StartPointer,FreeListPtr)
    Option = GetOption()
      
      
