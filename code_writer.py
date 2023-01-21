from parser import C_PUSH


class CodeWriter:
  ### Generates assembly code from the parsed VM command (note singular)

  def __init__(self, output_file):
    ### Opens the output file/stream and gets ready to write into it
    self._output_file = open(output_file, 'w')
    self._output_file.write(f"//{output_file.split('/').pop()}")
    self._eq_index = 0
    self._gt_index = 0
    self._lt_index = 0

    self._file_name = output_file.split('/')[-1].split('.')[0]

  def write_arithmetic(self, command):  #str
    ### Writes to the output file the assembly code that implements
    ### the given arithmetic command.

    if command == "add":
      self._output_file.writelines(_write_add())
    elif command == "sub":
      self._output_file.writelines(_write_sub())
    elif command == "neg":
      self._output_file.writelines(_write_neg())
    elif command == "eq":
      self._output_file.writelines(_write_eq(self._eq_index))
      self._eq_index += 1
    elif command == "gt":
      self._output_file.writelines(_write_gt(self._gt_index))
      self._gt_index += 1
    elif command == "lt":
      self._output_file.writelines(_write_lt(self._lt_index))
      self._lt_index += 1
    elif command == "and":
      self._output_file.writelines(_write_and())
    elif command == "or":
      self._output_file.writelines(_write_or())
    elif command == "not":
      self._output_file.writelines(_write_not())

  def write_push_pop(self, command, segment, index):
    ### Writes to the output file the assembly code that implements
    ### the given command given, where command is either C_PUSH or C_POP.
    if command == C_PUSH:
      self._output_file.writelines(_write_push(segment, index,
                                               self._file_name))
    else:
      self._output_file.writelines(_write_pop(segment, index, self._file_name))

  def close(self):
    ### Closes the output file/stream
    self._output_file.close()


def _write_add():  # PASSED
  ### Returns the assembly code that implements the add command.
  add = [
    "\n// add\n", "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "AM=M-1\n", "M=D+M\n",
    "@SP\n", "M=M+1\n"
  ]
  return add


def _write_sub():
  sub = [
    '\n// sub\n', "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "AM=M-1\n", "M=M-D\n",
    "@SP\n", "M=M+1\n"
  ]
  return sub


def _write_neg():
  neg = ["@SP\n", "A=M-1\n", "M=-M\n"]
  return neg


def _write_gt(gt_index):
  ### Returns the assembly code that implements the gt command
  gt = [
    "\n// gt\n", "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "A=M-1\n", "D=M-D\n",
    "M=-1\n", f"@GT_TRUE_{gt_index}\n", "D;JGT\n", "@SP\n", "A=M-1\n", "M=0\n",
    f"(GT_TRUE_{gt_index})\n"
  ]
  return gt


def _write_lt(lt_index):
  ### Returns the assembly code that implements the lt command
  lt = [
    "\n// lt\n", "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "A=M-1\n", "D=M-D\n",
    "M=-1\n", f"@LT_TRUE_{lt_index}\n", "D;JLT\n", "@SP\n", "A=M-1\n", "M=0\n",
    f"(LT_TRUE_{lt_index})\n"
  ]
  return lt


def _write_eq(eq_index):
  ### Returns the assembly code that implements the eq command
  eq = [
    "\n// eq\n", "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "A=M-1\n", "D=M-D\n",
    "M=-1\n", f"@EQ_TRUE_{eq_index}\n", "D;JEQ\n", "@SP\n", "A=M-1\n", "M=0\n",
    f"(EQ_TRUE_{eq_index})\n"
  ]
  return eq


def _write_and():
  command = [
    '\n// and\n', "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "A=M-1\n", "M=D&M\n"
  ]
  return command


def _write_or():
  command = [
    '\n// or\n', "@SP\n", "AM=M-1\n", "D=M\n", "@SP\n", "A=M-1\n", "M=D|M\n"
  ]
  return command


def _write_not():
  command = ['\n// not\n', "@SP\n", "A=M-1\n", "M=!M\n"]
  return command


def _write_push(segment, index, output_file):
  ### Return the assembly command for the push command depending on the segment and
  ### index.
  command = "push"
  if segment == "constant":
    push_constant = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@SP\n",
      "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_constant
  elif segment == "local":
    push_local = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@LCL\n",
      "A=M+D\n", "D=M\n", "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_local
  elif segment == "argument":
    push_argument = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@ARG\n",
      "A=M+D\n", "D=M\n", "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_argument
  elif segment == "this":
    push_this = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@THIS\n",
      "A=M+D\n", "D=M\n", "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_this
  elif segment == "that":
    push_that = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@THAT\n",
      "A=M+D\n", "D=M\n", "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_that
  elif segment == "static":
    push_static = [
      f"\n//{command} {segment} {index}\n", f"@{output_file}.{index}\n",
      "D=M\n", "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_static
  elif segment == "temp":
    temp = 5 + int(index)
    push_temp = [
      f"\n//{command} {segment} {index}\n", f"@{temp}\n", "D=M\n", "@SP\n",
      "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_temp
  elif segment == "pointer":
    this_or_that = ""
    if index == "0":
      this_or_that = "THIS"
    elif index == "1":
      this_or_that = "THAT"
    push_pointer = [
      f"\n//{command} {segment} {index}\n", f"@{this_or_that}\n", "D=M\n",
      "@SP\n", "A=M\n", "M=D\n", "@SP\n", "M=M+1\n"
    ]
    return push_pointer


def _write_pop(segment, index, output_file):
  ### Return the assembly command for the pop command depending on the segment and
  ### index.
  command = "pop"
  if segment == "local":
    pop_local = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@LCL\n",
      "D=M+D\n", "@R13\n", "M=D\n", "@SP\n", "AM=M-1\n", "D=M\n", "@R13\n",
      "A=M\n", "M=D\n"
    ]
    return pop_local
  elif segment == "argument":
    pop_argument = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@ARG\n",
      "D=M+D\n", "@R13\n", "M=D\n", "@SP\n", "AM=M-1\n", "D=M\n", "@R13\n",
      "A=M\n", "M=D\n"
    ]
    return pop_argument
  elif segment == "this":
    pop_this = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@THIS\n",
      "D=M+D\n", "@R13\n", "M=D\n", "@SP\n", "AM=M-1\n", "D=M\n", "@R13\n",
      "A=M\n", "M=D\n"
    ]
    return pop_this
  elif segment == "that":
    pop_that = [
      f"\n//{command} {segment} {index}\n", f"@{index}\n", "D=A\n", "@THAT\n",
      "D=M+D\n", "@R13\n", "M=D\n", "@SP\n", "AM=M-1\n", "D=M\n", "@R13\n",
      "A=M\n", "M=D\n"
    ]
    return pop_that
  elif segment == "static":
    pop_static = [
      f"\n//{command} {segment} {index}\n", "@SP\n", "AM=M-1\n", "D=M\n",
      f"@{output_file}.{index}\n", "M=D\n"
    ]
    return pop_static
  elif segment == "temp":
    temp = 5 + int(index)
    pop_temp = [
      f"\n//{command} {segment} {index}\n", "@SP\n", "AM=M-1\n", "D=M\n",
      f"@{temp}\n", "M=D\n"
    ]
    return pop_temp
  elif segment == "pointer":
    this_or_that = ""
    if index == "0":
      this_or_that = "THIS"
    elif index == "1":
      this_or_that = "THAT"
    pop_pointer = [
      f"\n//{command} {segment} {index}\n", "@SP\n", "AM=M-1\n", "D=M\n",
      f"@{this_or_that}\n", "M=D\n"
    ]
    return pop_pointer
