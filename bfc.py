import os
import sys
if len(sys.argv) < 3: print("py main.py file.bf language|py|go"); sys.exit(0)
if not sys.argv[1].endswith(".bf"): print("Only .bf files allowed"); sys.exit(0)
from src.Lexer import Lexer
from src.Parser import Parser
from src.Compiler import Compiler, CompilerGo, CompilerPy
from src.VirtualMachine import VirtualMachine
tokens = Lexer(sys.argv[1]).Tokenize()
program = Parser(tokens).ProduceAst()
end = sys.argv[2]
compiler = CompilerGo()
match end.lower().strip():
    case "go": pass
    case "py":
        compiler = CompilerPy()
        end = "go"
    case _:
        compiler = CompilerGo()
        end = "go"
f = open(sys.argv[1].replace(".bf", "."+end), "w")
for x in compiler.Compile(program).Code:
    f.write(x)
f.close()