class Node():
    Shifter     = 0
    Manipulator = 1
    InputOutput = 2
    Looping     = 3
    Program     = 4
    
    def __init__(self, NodeType, Token):
        self.NodeType = NodeType
        self.Token = Token

    def __init_loop__(self, Stmts):
        self.Stmts = Stmts
        return self
    
    def __init_program__(self, Program):
        self.Stmts = Program.getNodes()
        return self

class Program():
    
    def __init__(self) -> None: self.Nodes = []
    def add(self, Node): self.Nodes.append(Node); return self
    def getNodes(self) -> list[Node]: return self.Nodes
    def setNodes(self, Nodes): self.Nodes = Nodes; return self
