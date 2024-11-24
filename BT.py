class Node:
    def __init__(self):
        self.LeftPointer = -1
        self.Data = ""
        self.RightPointer = -1

    def GetLeft(self):
        return self.LeftPointer
    def GetData(self):
        return self.Data
    def GetRight(self):
        return self.RightPointer
    def SetLeft(self,Left):
        self.LeftPointer = Left
    def SetData(self,Data):
        self.Data = Data
    def SetRight(self,Right):
        self.RightPointer = Right

class TreeClass:
    def __init__(self):
        self.Tree = [Node() for i in range(0,19)]
        self.FirstNode = -1
        self.NumberNodes = 0
    def InsertNode(self,NewNode):
        if(self. NumberNodes == 0):
            self. Tree[0] = NewNode 
            self. FirstNode = 0
            self. NumberNodes = self. NumberNodes + 1
        else:
            self. Tree[self. NumberNodes] = NewNode
            NodeAccess = self. FirstNode
            Direction = ""
        while(NodeAccess != -1):
            Previous = NodeAccess
            if NewNode.GetData() < self. Tree[NodeAccess].GetData():
                NodeAccess = self. Tree[NodeAccess].GetLeft()
                Direction = "left"
            elif NewNode.GetData() > self. Tree[NodeAccess].GetData():
                NodeAccess = self. Tree[NodeAccess].GetRight()
                Direction = "right"
        if(Direction == "left"):
            self. Tree[Previous].SetLeft(self. NumberNodes)
        else:
            self. Tree[Previous].SetRight(self. NumberNodes)
            self. NumberNodes = self. NumberNodes + 1
    def OutputTree(self):
        if self. NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(0, self. NumberNodes):
                print(self. Tree[x].GetLeft(), " ", self. Tree[x].GetData(), " ",self.Tree[x].GetRight())
