import os
import time
import json

class File ():
    
    def __init__(self, name) -> None:
        self.name = name

    # acessors and mutators
    def getName(self) -> None:
        self._name = self.name

    def setName(self) -> str:
        return self._name

    # modules
    def createFolder(self) -> None:
        # creates a folder with the name and date of analysis of the filename

        # TODO fix so that the time is appended with month/day/year/time
        path = os.path.join(".", self.name + time.localtime())
        os.mkdir(path)


    def neuterFile(self) -> None:
        # defangs the malware by adding a file exenstion to it

        # TODO check to make sure it works
        os.rename(self.name, self.name + ".malw")

    def depositFile(self) -> None:
        # TODO puts all the info together into createFolder directory
        pass

    def displayResults(self) -> None:
        # display the results of the json recived from vt

        # TODO take the data from the json response and format into a table for viewing
        pass

