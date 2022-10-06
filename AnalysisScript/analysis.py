from sys import argv
import gui.py
from windows.py import windowsTools
from linux.py import linuxTools
import gui.py

# called if the imput to the program is wrong or if called
# by using -h
def usage(first_param):
    if first_param == "-h":
        # add all usage for the tools that require flags passed?
        print("usage: python3 analysis.py <file_name>")

    print("usage: python3 analysis.py <file_name>")
    

file_name = argv[1]
if argv[1] == None or "-h":
    usage(argv[1])

# need to check which os is running
if platform.system() = "Windows":
    windowsTools(file_name)
    # tool list will be based on FlareVM

if platform.system() = "Linux":
    linuxTools(file_name)
    # tools will be based on REMnux

