#!/usr/bin/env python
import sys
import os
from vm_translator import VMTranslator


def main():
  # Receive file path from stdin
  if len(sys.argv) == 2:
    path = sys.argv[1]
    if not os.path.exists(path):
      print("File not found")
    else:
      # Instantiate VMTranslator
      vmt = VMTranslator(path)
      vmt.translate()
  else:
    print("Missing Argument: Expected exactly one path to a file or directory")


if __name__ == '__main__':
  main()
