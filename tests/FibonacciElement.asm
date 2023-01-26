//FibonacciElement.asm
//push constant 786
@786
D=A
@SP
A=M
M=D
@SP
M=M+1

//push argument 6999
@6999
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LT_TRUE_0
D;JLT
@SP
A=M-1
M=0
(LT_TRUE_0)

//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

// add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
