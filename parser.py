import re
C_ARITHMETIC = "C_ARITHMETIC"
C_PUSH = "C_PUSH"
C_POP = "C_POP"

class Parser: # PASSED VERSION 1
  ### Handles the parsing of a single .vm file
  ### Reads a VM command, parses the command into its lexical components,
  ### and provides convenient access to these components.
  ### Ignores all white space and comments.
  
  def __init__(self, input_file):
    ### Opens the input file and gets ready to parse it
    self._lines = _open_file(input_file)
    self._current_command = None
    self._index = 0

  def has_more_commands(self): # PASSED
    ### Returns whether or not there are more commands to parse
    if not self._lines:
      return False
    elif self._index > len(self._lines) - 1:
      return False
    return True

  def advance(self): # PASSED
    ### Reads the next command from the input and makes it the
    ### current command.  It should be called only if has_more_commands()
    ### returns true.  Initially, the current command is None.
    if self.has_more_commands():
      self._current_command = self._lines[self._index]
      self._index += 1
    else:
      raise Exception("No more commands")

  def command_type(self): # PASSED
    ### Returns a constant representing the type of the current command.
    ### C_ARITHMETIC is returned for all the arithmetic/logical commands
    if ("push" in self._current_command):
      return C_PUSH
    elif ("pop" in self._current_command):
      return C_POP
    else:
      return C_ARITHMETIC

  def arg1(self): # PASSED
    ### Returns the first argument of the _current_command.  In the case of 
    ### C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
    ### Should not be called if the current command is C_RETURN.
    if self.command_type() == C_ARITHMETIC:
      return self._current_command
    else:
      return self._current_command.split(" ")[1]

  def arg2(self): # PASSED
    ### Returns the second argument of the current command.  Should be called
    ### only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
    valid_commands = [C_PUSH, C_POP]
    if self.command_type() not in valid_commands:
      raise Exception("Invalid command")
    else:
      return self._current_command.split(" ")[2]

  ### TESTING FUNCTIONS
  def get_current_command(self):
    ### Prints the current command
    return self._current_command

  def get_index(self):
    ### Prints the current index
    return self._index


    
### HELPER FUNCTIONS        
def _open_file(file_path):
  ### Opens file and removes whitespace
  lines = []
  with open(file_path, 'r') as f:
    lines = f.readlines()
  
  lines = [_remove_whitespace(line) for line in lines]
  lines = [line for line in lines if line]
  return lines

def _remove_whitespace(line):
    pattern = r'//.*'
    line = re.sub(pattern, '', line)
    line = line.strip()
    return line


  
### TESTS ###
def _test_parser(file):
  parser = Parser(file)
  arg2_cmds = [C_PUSH, C_POP]
  
  print("######TESTING PARSER######")
  for i in range(50):
    parser.advance() 
    print(f"\ncurrent_command: {parser.get_current_command()}")
    print(f"command_type: {parser.command_type()}")
    print(f"arg1: {parser.arg1()}")
    if parser.command_type() in arg2_cmds:
      print(f"arg2: {parser.arg2()}")
    print(f"has_more_commands: {parser.has_more_commands()}")
    print(f"index: {parser.get_index()}")

    
def _test_open_file(file):
  lines = _open_file(file)
  print(lines)

# _test_open_file("test.vm") PASSED
# _test_parser("test.vm") PASSED

