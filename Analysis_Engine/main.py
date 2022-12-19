#!/usr/bin/python3

from vtlookup import lookup
from filehandle import File
from unpacme import unpac
from signature import *
import os

VTDoclink = "https://developers.virustotal.com/reference/overview"
# since most of the tools are already in REMnux
REMnuxlink = "https://docs.remnux.org/"

# displays the banner on startup
def banner() -> None:
    termSize = os.get_terminal_size()
    print("Some thing here for now")

# run evertime
# check for complete setup
def setup() -> None:
    path = os.path.join(".", "DataBase")
    os.mkdir(path)

    banner()

def main () -> None:
    
    userInput = ""
    while(userInput.lower() != "q" or "quit"):
        print("RE_Engine: ", end="")
        
        userInput = str(input())

        # filename comes from input in the shell
        file = File("test") 
        lookup(file)

        # utilize unpacme to get the unpacked verison of the malware
        if (packed == True):
           unpac(file) 
        
        # generate the signatures and store in the DataBase
        gensignature()
        store()

        # defang the malware and store it away
        file.neuterFile()
        file.createFolder()
   
    
