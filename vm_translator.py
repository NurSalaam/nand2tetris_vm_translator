import os
from parser import Parser, C_ARITHMETIC, C_PUSH, C_POP
from code_writer import CodeWriter




class VMTranslator:

  def __init__(self, input_path):
    if ".vm" in input_path:
      # i.e. path is to a file
      output_path = input_path.replace(".vm", ".asm")
      self._files = [input_path]
      self._dir = '.'
    else:
      # i.e. path is to a directory
      output_path = input_path + ".asm"
      temp = os.listdir(input_path)
      self._files = [file for file in temp if '.vm' in file]
      self._dir = input_path
    self._output_path = output_path

    # Construct a CodeWriter to handle the output_file.
    self._code_writer = CodeWriter(self._output_path)

  def translate(self):
    print(self._files)
  
    for file in self._files:
      path = f"{self._dir}/{file}"
      print(f"Parsing {path}...")
    
      # Construct a Parser to handle the input_file.
      parser = Parser(path)
      
      # Marches through the input file, parsing each line and generating code from it.
      while parser.has_more_commands():
        # March
        parser.advance()
        # Switch on parser.command_type()
        if parser.command_type() == C_ARITHMETIC:
          command = parser.arg1()
          self._code_writer.write_arithmetic(command)
        elif (parser.command_type() == C_PUSH) or (parser.command_type()
                                                   == C_POP):
          command = parser.command_type()
          segment = parser.arg1()
          index = parser.arg2()
          self._code_writer.write_push_pop(command, segment, index)
        else:
          pass

    # Close file
    self._code_writer.close()
