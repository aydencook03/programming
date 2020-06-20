#! /usr/bin/python

import sys

name = None

try:
    # sys.argv[1] is the string typed after the name of the script --> python passingArguments.py _FILENAME_
    with open(sys.argv[1]) as f:
        print(f.read())
except:
    print("Type a file name after the script name to see its contents")
