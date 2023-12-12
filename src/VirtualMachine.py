from src.Compiler import Compiler

class Cells():
    def __init__(self, PtrMax, CellMax) -> None:
        self.ptr = 0
        self.cells = [0]*PtrMax
        self.PtrMax = PtrMax
        self.CellMax = CellMax
        self.Highest = 0
        
    def IncrementPointer(self):
        self.ptr += 1
        if self.ptr > self.Highest-1: self.Highest = self.ptr+1
        if self.ptr > self.PtrMax-1: self.ptr = 0
        
    def DecrementPointer(self):
        self.ptr -= 1
        if self.ptr < 0: self.ptr = self.PtrMax-1
        
    def IncrementCell(self):
        self.cells[self.ptr] += 1
        if self.cells[self.ptr] > self.CellMax-1: self.cells[self.ptr] = 0
        
    def DecrementCell(self):
        self.cells[self.ptr] -= 1
        if self.cells[self.ptr] < 0: self.cells[self.ptr] = self.CellMax-1
        
    def SetCell(self, cell): self.cells[self.ptr] = cell
        
    def GetCell(self):
        return self.cells[self.ptr]

class VirtualMachine():
    
    def __init__(self, Bytecode) -> None:
        self.ptr = 0
        self.Bytecode = Bytecode
        self.Highest = 80000
        
    def Run(self):
        self.ptr = 0
        self.Cells = Cells(1000, 256)
        while self.ptr <= len(self.Bytecode)-1:
            match self.Bytecode[self.ptr]:
                case Compiler.INCREMENT: self.Cells.IncrementCell(); self.ptr += 1
                case Compiler.DECREMENT: self.Cells.DecrementCell(); self.ptr += 1
                case Compiler.SHIFT_RIGHT: self.Cells.IncrementPointer(); self.ptr += 1
                case Compiler.SHIFT_LEFT: self.Cells.DecrementPointer(); self.ptr += 1
                case Compiler.JUMP_ZERO:
                    self.ptr += 2
                    if self.Cells.GetCell() == 0:
                        self.ptr = self.Bytecode[self.ptr-1]
                case Compiler.JUMP_NONZERO:
                    self.ptr += 2
                    if self.Cells.GetCell() != 0:
                        self.ptr = self.Bytecode[self.ptr-1]
                case Compiler.OUTPUT_BYTE:
                    print(chr(self.Cells.GetCell()), end="")
                    self.ptr += 1
                case Compiler.INPUT_BYTE:
                    self.Cells.SetCell(ord(list(input("\n: "))[0]))
                    self.ptr += 1
        return self