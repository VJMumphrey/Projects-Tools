#!/usr/bin/python3
import VTlookup
import FileHandle

VTDoclink = "https://developers.virustotal.com/reference/overview"
# since most of the tools are already in REMnux
REMnuxlink = "https://docs.remnux.org/"
def main ():
    """
    CLI Analysis Engine that will perform a myriad of basic analysis and malware handling in order to speed up malware analysis
        - VirusTotal lookup using the api library
        - Pull strings and rank them Using String Sifter (Flare)
        - FLoss to extract potentially more strings
        - Use yara rules to classify rules
        - Develop the yara rules for the sample
        - generate hashes that aren't pulled from VirusTotal
        - Yara Rules to identify common malicious capabilities
        - Re-search.py tp search for possible regex and sus artifacts
        - ClamAV
        - Defang the malare by adding ".malw" to the file
        - package it in .zip folder for transport with password

    Dump files into directory named with time and date and malware name
        - store the info from virus total and defanged sample for further in-depth analysis later

    """

