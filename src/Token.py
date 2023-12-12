class Token():
    
    SHIFT_RIGHT = 0 # ">"
    SHIFT_LEFT  = 1 # "<"
    INCREMENT   = 3 # "+"
    DECREMENT   = 4 # "-"
    INPUT_BYTE  = 5 # ","
    OUTPUT_BYTE = 6 # "."
    START_LOOP  = 7 # "["
    END_LOOP    = 8 # "]"
    EOF         = 9 # "End Of File"
    
    def __init__(self, Type):
        self.Type = Type