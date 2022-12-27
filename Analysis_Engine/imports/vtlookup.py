import vt
import hashlib

# used to lookup info about a file
# scan it if info is old or not existent
def lookupFile(malw):

    client = vt.Client("API")
    file = client.get_object(malw.path) 

    client.close()

# used to lookup a url
# called by user input in shell
def lookupUrl(url):
    pass
    
# used to lookup a domain
def lookupDomain(domain):
    pass

# send the file to be scanned and wait for results
def scanFile(malw):
    pass
