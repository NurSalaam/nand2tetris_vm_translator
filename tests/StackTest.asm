//StackTest.asm
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@EQ_TRUE_0
D;JEQ
@SP
A=M-1
M=0
(EQ_TRUE_0)

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@EQ_TRUE_1
D;JEQ
@SP
A=M-1
M=0
(EQ_TRUE_1)

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@EQ_TRUE_2
D;JEQ
@SP
A=M-1
M=0
(EQ_TRUE_2)

//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
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

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 892
@892
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
@LT_TRUE_1
D;JLT
@SP
A=M-1
M=0
(LT_TRUE_1)

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
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
@LT_TRUE_2
D;JLT
@SP
A=M-1
M=0
(LT_TRUE_2)

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@GT_TRUE_0
D;JGT
@SP
A=M-1
M=0
(GT_TRUE_0)

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@GT_TRUE_1
D;JGT
@SP
A=M-1
M=0
(GT_TRUE_1)

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@GT_TRUE_2
D;JGT
@SP
A=M-1
M=0
(GT_TRUE_2)

//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 53
@53
D=A
@SP
A=M
M=D
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

//push constant 112
@112
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
@SP
A=M-1
M=-M

// and
@SP
AM=M-1
D=M
@SP
A=M-1
M=D&M

//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
AM=M-1
D=M
@SP
A=M-1
M=D|M

// not
@SP
A=M-1
M=!M
