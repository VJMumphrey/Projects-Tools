### TODO

main:
create and run the shell like interface
- input system with specific commands
	- create a banner for the shell on startup
	- displayResults from the scan in a table(filehandle.displayresults)
	- save the results
	- build out shell system
	- help menu and such for the shell
	- take input from vtlookup to help and determine if the sample is packed
	- submitting file needs to use path

filehandle:
displayResults
    - take the data from the json response and format into a table for viewing

depositFile
	- put all the info together into createFolder directory

neuterFile
	- test to make sure it is working properly
	- remove executeability on the different operating systems?

createFolder
	- fix so that the time is appended with month/day/year/time

vtlookup:
	- finish file submission system
    - finish url system
    - build shell functionalty

unpac:
	- build out unpac 

signature:
	- (later) implement hashing system to determine if files are simular or the same
	- used to build database of malware geneology of functions and capabilities
	- hashing of functions? need to find a way of doing this without getting thrown off from obfuscation
	- test out engines. will only be for x64 arch for now. different files for each arch
	- seperate files and calls for different archs