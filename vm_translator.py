import os
from parser import Parser, C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_CALL, C_RETURN
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
      self._code_writer.set_file_name(file)
      path = f"{self._dir}/{file}"
      print(f"Parsing {path}...")
    
      # Construct a Parser to handle the input_file.
      parser = Parser(path)
      
      # Marches through the input file, parsing each line and generating code from it.
      while parser.has_more_commands():
        # March
        parser.advance()
        # Switch on parser.command_type()
        command_type = parser.command_type()
        if command_type == C_ARITHMETIC:
          command = parser.arg1()
          self._code_writer.write_arithmetic(command)
        elif (command_type == C_PUSH) or (command_type
                                                   == C_POP):
          command = command_type
          segment = parser.arg1()
          index = parser.arg2()
          self._code_writer.write_push_pop(command, segment, index)
        elif command_type == C_LABEL:
          label = parser.arg1()
          self._code_writer.write_label(label)
        elif command_type == C_GOTO:
          label = parser.arg1()
          self._code_writer.write_goto(label)
        elif command_type == C_IF:
          label = parser.arg1()
          self._code_writer.write_if(label)
        else:
          raise NotImplementedError('Implement switch on Branching and Function commands')

    # Close file
    self._code_writer.close()
