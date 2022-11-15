#!/usr/bin/python3
from vtlookup import lookup
from filehandle import File
import os
from unpacme import unpac

VTDoclink = "https://developers.virustotal.com/reference/overview"
# since most of the tools are already in REMnux
REMnuxlink = "https://docs.remnux.org/"

def setup() -> None:
    # TODO create a directory for the malware and its results if not already created
    path = os.path.join(".", "DumpFolder")
    os.mkdir(path)

def main () -> int:
    """
    create and run the shell like interface
    - input system with specific commands
        - startup (warns if DumpFolder is already created)
        - input file
        - displayResults from the scan in a table
        - save the results
        - help menu and such for the shell
        - exit the shell
    """

    # filename comes from input in the shell
    file = File("test") 
    lookup(file)

    # TODO packed will come from the json response in vtlookup
    if (packed == True):
       unpac(file) 
    
    file.neuterFile()
    file.createFolder()
    
    return 0;

    

    

