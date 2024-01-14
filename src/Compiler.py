from src.Ast import Node, Program
from src.Token import Token
class Compiler():
    
    INCREMENT    = 0
    DECREMENT    = 1
    SHIFT_RIGHT  = 2
    SHIFT_LEFT   = 3
    OUTPUT_BYTE  = 4
    INPUT_BYTE   = 5
    JUMP_NONZERO = 6
    JUMP_ZERO    = 7
    
    def __init__(self) -> None:
        self.Bytecode = []
    
    def Emit(self, Mnemonic, Oprand = None) -> int:
        index = len(self.Bytecode)
        self.Bytecode.append(Mnemonic)
        if Oprand != None: self.Bytecode.append(Oprand)
        return index
    
    def Replace(self, Addr, Mnemonic, Oprand = None) -> int:
        self.Bytecode[Addr] = Mnemonic
        if Oprand != None: self.Bytecode[Addr+1] = Oprand
        return Addr
    
    def Compile(self, node):
        match node.NodeType:
            case Node.Program:
                for stmt in node.Stmts:
                    self.Compile(stmt)
            case Node.Looping:
                Start = self.Emit(self.JUMP_ZERO, 69)
                for stmt in node.Stmts:
                    self.Compile(stmt)
                Addr = self.Emit(self.JUMP_NONZERO, Start)
                self.Replace(Start, self.JUMP_ZERO, Addr)
            case Node.Manipulator:
                match node.Token.Type:
                    case Token.INCREMENT: self.Emit(self.INCREMENT)
                    case Token.DECREMENT: self.Emit(self.DECREMENT)
            case Node.Shifter:
                match node.Token.Type:
                    case Token.SHIFT_LEFT: self.Emit(self.SHIFT_LEFT)
                    case Token.SHIFT_RIGHT: self.Emit(self.SHIFT_RIGHT)
            case Node.InputOutput:
                match node.Token.Type:
                    case Token.INPUT_BYTE: self.Emit(self.INPUT_BYTE)
                    case Token.OUTPUT_BYTE: self.Emit(self.OUTPUT_BYTE)
            case _:
                raise Exception("Unknown Node type "+str(node.NodeType))
            
        return self
    
class CompilerGo():
    
    def __init__(self) -> None:
        self.Code = [
            "package main;",
            "import \"fmt\";",
            "var ptr int = 0;",
            "var cells []byte = make([]byte, 1000);",
            "func incPtr() { ptr += 1; if ptr > 999{ptr = 0}; };",
            "func decPtr() { ptr -= 1; if ptr < 0 { ptr = 999} };",
            "func incCell() { cells[ptr] += 1; if cells[ptr] > 255 {cells[ptr] = 0} };",
            "func decCell() { cells[ptr] -= 1; if cells[ptr] < 0 {cells[ptr] = 255} };",
            "func SetCell(cell byte) {cells[ptr] = cell};",
            "func GetCell() byte { return cells[ptr] };",
            "func outputCell() { fmt.Print(string(GetCell())) };",
            "func inputCell() { var s string; fmt.Print(\"\\n:\"); fmt.Scanln(&s); SetCell(byte(s[0])); fmt.Print(\"\\n\") };"
            "func main() {",
        ]
    def Emit(self, Mnemonic): self.Code.append(Mnemonic)
    
    def Compile(self, node):
        self.__compile__(node)
        self.Emit("}")
        return self
    
    def __compile__(self, node):
        match node.NodeType:
            case Node.Program:
                for stmt in node.Stmts:
                    self.__compile__(stmt)
            case Node.Looping:
                self.Emit("for cells[ptr] != 0 {")
                for stmt in node.Stmts:
                    self.__compile__(stmt)
                self.Emit("};")
            case Node.Manipulator:
                match node.Token.Type:
                    case Token.INCREMENT: self.Emit("incCell();")
                    case Token.DECREMENT: self.Emit("decCell();")
            case Node.Shifter:
                match node.Token.Type:
                    case Token.SHIFT_LEFT: self.Emit("incPtr();")
                    case Token.SHIFT_RIGHT: self.Emit("decPtr();")
            case Node.InputOutput:
                match node.Token.Type:
                    case Token.INPUT_BYTE: self.Emit("inputCell();")
                    case Token.OUTPUT_BYTE: self.Emit("outputCell();")
            case _:
                raise Exception("Unknown Node type "+str(node.NodeType))
            
        return self
    
class CompilerPy():
    
    depth = 0

    def __init__(self) -> None:
        self.Code = [
            """ptr = 0
cells = [0] * 1000
def incPtr():
    global ptr
    ptr += 1
    if ptr > 999:
        ptr = 0
def decPtr():
    global ptr
    ptr -= 1
    if ptr < 0:
        ptr = 999
def incCell():
    cells[ptr] += 1
    if cells[ptr] > 255:
        cells[ptr] = 0
def decCell():
    cells[ptr] -= 1
    if cells[ptr] < 0:
        cells[ptr] = 255
def SetCell(cell): cells[ptr] = cell
def GetCell(): return cells[ptr]
def outputCell(): print(chr(GetCell()), end = \"\")
def inputCell(): SetCell(input(\"\\n:\")[0])""",
        ]
    def Emit(self, Mnemonic): self.Code.append(Mnemonic)
    
    def Compile(self, node):
        self.__compile__(node)
        self.Emit("\n")
        return self
    
    def __do_deapth__(self):
        return "\n" + (self.depth * "\t")
    
    def __compile__(self, node):
        match node.NodeType:
            case Node.Program:
                for stmt in node.Stmts:
                    self.__compile__(stmt)
            case Node.Looping:
                self.Emit(self.__do_deapth__()+"while cells[ptr] != 0:")
                self.depth += 1
                for stmt in node.Stmts:
                    self.__compile__(stmt)
                self.depth -= 1
            case Node.Manipulator:
                match node.Token.Type:
                    case Token.INCREMENT: self.Emit(self.__do_deapth__()+"incCell()")
                    case Token.DECREMENT: self.Emit(self.__do_deapth__()+"decCell()")
            case Node.Shifter:
                match node.Token.Type:
                    case Token.SHIFT_LEFT: self.Emit(self.__do_deapth__()+"incPtr()")
                    case Token.SHIFT_RIGHT: self.Emit(self.__do_deapth__()+"decPtr()")
            case Node.InputOutput:
                match node.Token.Type:
                    case Token.INPUT_BYTE: self.Emit(self.__do_deapth__()+"inputCell()")
                    case Token.OUTPUT_BYTE: self.Emit(self.__do_deapth__()+"outputCell()")
            case _:
                raise Exception("Unknown Node type "+str(node.NodeType))
            
        return self