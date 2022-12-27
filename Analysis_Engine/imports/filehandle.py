import os
import time
import json

class File ():
    
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path

    # -- acessors and mutators --
    @property
    def setName(self) -> str:
        return self._name

    @property
    def setPath(self) -> str:
        return self.path

    @setName.setter
    def getName(self) -> None:
        self._name = self.name

    @setPath.setter
    def getPath(self) -> None:
        self._path = self.path


    # -- methods -- 
    def createFolder(self) -> None:
        # creates a folder with the name and date of analysis of the filename

        path = os.path.join(".", self.name + time.localtime())
        os.mkdir(path)

    def neuterFile(self) -> None:
        # defangs the malware by adding a file exenstion to it
        os.rename(self.name, self.name + ".malw")

    def depositFile(self) -> None:
        pass

    def displayResults(self) -> None:
        # display the results of the json recived from vt
        pass

