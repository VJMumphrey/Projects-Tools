#!/usr/bin/python3

from vtlookup import *
from filehandle import File
from unpacme import unpac
from signature import *
import os

# since most of the tools are already in REMnux
REMnuxlink = "https://docs.remnux.org/"


# displays the banner on startup
def banner() -> None:
    termSize = os.get_terminal_size()
    print("Some thing here for now")

# run everytime
# check for complete setup
def setup(folder_path) -> None:
    if os.path.exists(folder_path + "/DataBase"):
        pass
    else:
        os.mkdir(folder_path + "/DataBase")

    if os.path.exists(folder_path + "/DumpFolder"):
        pass
    else:
        os.mkdir(folder_path + "/DumpFolder")

    banner()

def main () -> None:
    main_folder_path = "~/RE_Engine"
    
    setup(main_folder_path)
    userInput = ""
    while(userInput.lower() != "q" or "quit"):
        print("RE_Engine: ", end="")
        
        userInput = str(input())
            
        if (userInput == "scan file"):
            # lookup info about the file
            lookupFile(file)
            # if there is no info, scan the file

        elif (userInput == "scan url"):
            # lookup the url
            lookupUrl("some url")

        elif (userInput == "lookup domain"):
            lookupDomain(domain)

        elif (userInput == "auto"):

        # filename comes from input in the shell
        file = File("test", inputFilePath) 
        lookupFile(file)

        # utilize unpacme to get the unpacked verison of the malware
        if (packed == True):
           unpac(file) 
        
        # generate the signatures and store in the DataBase
        gensignature()
        store()

        # defang the malware and store it away
        file.neuterFile()
        file.createFolder()
   
    
