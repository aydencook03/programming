#! /usr/bin/python

import sys
import os
import subprocess
import importlib
import shutil

try:
    fileToCompile = sys.argv[1]
except:
    fileToCompile = input('Enter File to be Compiled: ')

with open('setupFile.py', 'w') as f:
    f.write('from setuptools import setup\ntry:\n\tfrom Cython.Build import cythonize\n\n\tsetup(\n\t\text_modules = cythonize("{0}")\n\t)\nexcept:\n\tprint("You must have Cython installed")'.format(fileToCompile))

subprocess.run(["python", "setupFile.py", "build_ext", "--inplace"])
try:
    importlib.import_module(fileToCompile[0:-3])
except:
    print("File extension must be '.py'")
os.remove('setupFile.py')
try:
    os.remove(fileToCompile[0:-3] + '.c')
    os.remove(fileToCompile[0:-3] + '.cpython-38-x86_64-linux-gnu.so')
    shutil.rmtree('build')
except:
    print("Cython is not installed")
    shutil.rmtree('__pycache__')
