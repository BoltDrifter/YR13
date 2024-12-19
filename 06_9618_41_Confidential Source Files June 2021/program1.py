class Node:
    def __init__(self,Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer

LinkedList = [Node(1,1), Node(5,4), Node(6,7), Node(7,-1) , Node(2,2), Node(0,6), Node(0,8),Node(56,3), Node(0,9), Node(0,-1)]
StartPointer = 0
emptylist = 5

def outputNodes(Array, StartPointer):
    while StartPointer !=  -1:
        print(str(Array[StartPointer].Data))
        StartPointer = Array[StartPointer].Pointer

def addNodes(LinkedList, StartPointer, emptyList):
    data = input("Data: ")
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newnode = Node(int(data), -1)
        LinkedList[emptyList] = newnode

        previouspointer = 0
        while StartPointer != -1:
            previouspointer = StartPointer
            StartPointer = LinkedList[StartPointer].Pointer
        LinkedList[previouspointer].Pointer = emptyList
        emptyList = LinkedList[emptyList].Pointer
        return True


outputNodes(LinkedList, StartPointer)
returnValue = addNodes(LinkedList, StartPointer, emptylist)
if returnValue == True:
    print("Item successfully added")
else:
    print("Item not added, list full")
outputNodes(LinkedList, StartPointer)
