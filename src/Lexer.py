from src.Token import Token

class Lexer():
    
    def __init__(self, file) -> None:
        self.ptr = 0
        f = open(file, "r")
        self.chars = list(f.read())
        f.close()
        
    def __at__(self) -> str:
        if self.__eof__():
            return " "
        return self.chars[self.ptr]
    
    def __eof__(self) -> bool: return not (self.ptr <= len(self.chars)-1)
    def __ignore__(self) -> None:
        match self.__at__():
            case " ": self.ptr += 1
            case "\n": self.ptr += 1
            case "\r": self.ptr += 1
            case "\t": self.ptr += 1
            case "\a": self.ptr += 1
            case "\f": self.ptr += 1
            case "\v": self.ptr += 1
            case "\b": self.ptr += 1

    def Tokenize(self) -> list[Token]:
        tokens = []
        while not self.__eof__():
            self.__ignore__()
            TknType = None
            match self.__at__():
                case ">": TknType = Token.SHIFT_RIGHT; self.ptr+=1
                case "<": TknType = Token.SHIFT_LEFT; self.ptr+=1
                case ".": TknType = Token.OUTPUT_BYTE; self.ptr+=1
                case ",": TknType = Token.INPUT_BYTE; self.ptr+=1
                case "+": TknType = Token.INCREMENT; self.ptr+=1
                case "-": TknType = Token.DECREMENT; self.ptr+=1
                case "[": TknType = Token.START_LOOP; self.ptr+=1
                case "]": TknType = Token.END_LOOP; self.ptr+=1
                case _: self.ptr += 1
                
            if TknType != None: tokens.append(Token(TknType))
        tokens.append(Token(Token.EOF))
        
        return tokens