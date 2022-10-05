from sys import argv
import sh, os

file_name = argv[1]

print(sh.file(file_name))

