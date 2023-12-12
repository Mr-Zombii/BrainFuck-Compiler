# Brain Fuck Interpreter

This is a basic implimentation of the Esolang [BrainFuck](https://esolangs.org/wiki/Brainfuck) on a bytecode virtual machine that can be transpiled to [Golang](https://go.dev).

```shell
# Transpile your brainfuck program to Go
py bfc.py "File Here.bf"

# Run your brainfuck program in ther bytecode vm
# this approch is very slow transpiling is recommended
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