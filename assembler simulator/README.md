# Computer Organization Project: Assembler and Simulator
This is a project for the Computer Organization course, which aims to implement an assembler and simulator for a simple instruction set architecture (ISA).The ISA used in this project has a limited number of instructions, including arithmetic and logic operations, as well as memory access instructions.
The project aims to provide a toolset for converting assembly language programs into machine code and simulating the execution of these programs on a virtual computer.
This repository contains the source code for the assembler and simulator. 

## Assembler
The assembler is implemented in Python. The assembly file will be a text file which will be given as input from user that contains the assembly language code. The assembler will produce a machine code file with the name as machine_code
### Features
1. Converts assembly language programs into machine code.
2. Supports a range of instructions and addressing modes.
3. Comprehensive error handling to catch and report syntax errors, undefined labels, invalid instructions, and addressing mode mismatches.
4. Generation of a listing file with machine code, and error messages for debugging.
5. Clear and informative error messages with line numbers to pinpoint the location and nature of errors.


## Simulator
The simulator is implemented in Python. The machine code will be taken from stdin as input from user. The simulator will produce the simulation of the code.
### Features
1. Simulates the execution of machine code.
2. Provides a listing of the machine code and the simulated registers.
3. Provides a representation of the memory dump.
4. Provides a representation of the program counter.
