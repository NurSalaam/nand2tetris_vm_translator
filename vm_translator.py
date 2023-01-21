from parser import Parser, C_ARITHMETIC, C_PUSH, C_POP
from code_writer import CodeWriter


class VMTranslator:

  def __init__(self, input_path):
    self._input_path = input_path

    output_path = input_path.replace(".vm", ".asm")
    self._output_path = output_path

  def translate(self):
    # Construct a Parser to handle the input_file.
    parser = Parser(self._input_path)
    # Construct a CodeWriter to handle the output_file.
    code_writer = CodeWriter(self._output_path)
    # Marches through the input file, parsing each line and generating code from it.
    while parser.has_more_commands():
      # March
      parser.advance()
      # Switch on parser.command_type()
      if parser.command_type() == C_ARITHMETIC:
        command = parser.arg1()
        code_writer.write_arithmetic(command)
      elif (parser.command_type() == C_PUSH) or (parser.command_type()
                                                 == C_POP):
        command = parser.command_type()
        segment = parser.arg1()
        index = parser.arg2()
        code_writer.write_push_pop(command, segment, index)
      else:
        pass

    # Close file
    code_writer.close()
