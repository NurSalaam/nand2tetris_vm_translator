import os
from parser import Parser, C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_CALL, C_RETURN
from code_writer import CodeWriter




class VMTranslator:

  def __init__(self, input_path):
    if ".vm" in input_path:
      self.is_dir = False
      # i.e. path is to a file
      output_path = input_path.replace(".vm", ".asm")
      self._files = [input_path]
      self._dir = '.'
    else:
      # i.e. path is to a directory
      self.is_dir = True
      # path doesn't end in '/'
      self._dir = input_path
      output_path = input_path + '/' + input_path.split('/')[-1] + ".asm"
      
      if input_path[-1] == '/':
        # path ends in '/'
        self._dir = input_path[:-1]
        output_path = input_path[:-1] + '/' + input_path.split('/')[-2] + ".asm"
      
      temp = os.listdir(input_path)
      self._files = [file for file in temp if '.vm' in file]
      
    self._output_path = output_path
    print(output_path)

    # Construct a CodeWriter to handle the output_file.
    self._code_writer = CodeWriter(self._output_path)

  def translate(self):
    print(self._files)
    if self.is_dir:
      self._code_writer.write_init()
  
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
        elif command_type == C_FUNCTION:
          func_name = parser.arg1()
          num_vars = parser.arg2()
          self._code_writer.write_function(func_name, num_vars)
        elif command_type == C_RETURN:
          self._code_writer.write_return()
        elif command_type == C_CALL:
          func_name = parser.arg1()
          num_args = parser.arg2()
          self._code_writer.write_call(func_name, num_args)
        else:
          raise Exception("Unknown command type")

    # Close file
    self._code_writer.close()
