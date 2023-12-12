from src.Ast import Node, Program
from src.Token import Token

class Parser():
    
    def __init__(self, Tokens) -> None:
        self.ptr = 0
        self.Tokens = Tokens
    
    def __eof__(self) -> bool: return self.Tokens[self.ptr].Type == Token.EOF
    def __at__(self) -> Token: return self.Tokens[self.ptr]
    def __advance__(self) -> Token: self.ptr += 1; return self.Tokens[self.ptr-1]
    
    def __parse_manipulator__(self):
        token = self.__advance__()
        return Node(Node.Manipulator, token)
    
    def __parse_shifter__(self):
        token = self.__advance__()
        return Node(Node.Shifter, token)
    
    def __parse_input_output__(self):
        token = self.__advance__()
        return Node(Node.InputOutput, token)
    
    def __parse_loop__(self):
        token = self.__advance__()
        loop = []
        while self.__at__().Type != Token.END_LOOP:
            loop.append(self.__parse_stmt__())
        self.__advance__()
        return Node(Node.Looping, token).__init_loop__(loop)        
            
    
    def __parse_stmt__(self) -> Node:
        match self.__at__().Type:
            case Token.INCREMENT   : return self.__parse_manipulator__()
            case Token.DECREMENT   : return self.__parse_manipulator__()
            case Token.SHIFT_LEFT  : return self.__parse_shifter__()
            case Token.SHIFT_RIGHT : return self.__parse_shifter__()
            case Token.OUTPUT_BYTE : return self.__parse_input_output__()
            case Token.INPUT_BYTE  : return self.__parse_input_output__()
            case Token.START_LOOP  : return self.__parse_loop__()
            case _: raise Exception("Unknown Token " + str(self.__at__().Type))
    
    def ProduceAst(self):
        p = Program()
        firstToken = self.__at__()
        while not self.__eof__():
            p.add(self.__parse_stmt__())
        return Node(Node.Program, firstToken).__init_program__(p)