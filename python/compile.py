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
    f.write('from setuptools import setup\nfrom Cython.Build import cythonize\n\nsetup(\n\text_modules = cythonize("{0}")\n)'.format(fileToCompile))
    
subprocess.run(["python", "setupFile.py", "build_ext", "--inplace"])
try:
    importlib.import_module(fileToCompile[0:-3])
except:
    print("Extension must be '.py'")
os.remove('setupFile.py')
os.remove(fileToCompile[0:-3] + '.c')
os.remove(fileToCompile[0:-3] + '.cpython-38-x86_64-linux-gnu.so')
shutil.rmtree('build')
