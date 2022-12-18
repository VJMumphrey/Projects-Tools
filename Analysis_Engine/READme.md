## About
This project is something that I am going to try and work on. My goal is to eventually use this for my own work. There are some big ideas for this and it will definatley take some time

### TODO

main:
create and run the shell like interface
- input system with specific commands
    - startup (warns if DumpFolder is already created)
    - input file
	- displayResults from the scan in a table
	- save the results
	- help menu and such for the shell
	- exit the shell
	- take input from vtlookup to help and determine if the sample is packed

filehandle:
displayResults
    - take the data from the json response and format into a table for viewing

depositFile
	- put all the info together into createFolder directory

neuterFile
	- test to make sure it is working properly
	- remove executeability on the different OS?

createFolder
	- fix so that the time is appended with month/day/year/time

vtlookup:
	- finish and test out submission and return system

unpac:
	- build out unpac 

signature:
	- (later) implement hashing system to determine if files are simular or the same
	- used to build database of malware geneology of functions and capabilities
	- hashing of functions? need to find a way of doing this without getting thrown off from obfuscation
	- take look into incorporating Keystone Capstone and unicorn engines?
