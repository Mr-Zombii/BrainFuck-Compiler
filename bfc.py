import os
import sys
if len(sys.argv) < 2: print("py main.py file.bf"); sys.exit(0)
if not sys.argv[1].endswith(".bf"): print("Only .bf files allowed"); sys.exit(0)
from src.Lexer import Lexer
from src.Parser import Parser
from src.Compiler import Compiler, CompilerGo
from src.VirtualMachine import VirtualMachine
tokens = Lexer(sys.argv[1]).Tokenize()
program = Parser(tokens).ProduceAst()
f = open(sys.argv[1].replace(".bf", ".go"), "w")
for x in CompilerGo().Compile(program).Code:
    f.write(x)
f.close()