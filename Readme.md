# Brain Fuck Compiler

This is a basic implementation of the Esolang [BrainFuck](https://esolangs.org/wiki/Brainfuck) on a bytecode virtual machine that can be transpiled to [Golang](https://go.dev). If you want to see this but recreated on [Scratch](https://scratch.mit.edu) check [here](https://scratch.mit.edu/projects/938671954/). If you want the faster runtime check [here](https://turbowarp.org/938671954?turbo&fps=60).

```shell
# Transpile your brainfuck program to Go
py bfc.py "File Here.bf" go
# Transpile your brainfuck program to Python
py bfc.py "File Here.bf" py

# Run your brainfuck program in ther bytecode vm.
# sadly the bytecode vm is very slow for big programs
# and transpiling is recommended.
py bf.py "File Here.bf"
```
<br>
<br>
<br>

```
Hello world.bf
```

```bf
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```
### Output
```bat
Hello World!
```