import vt

# used to lookup info about a file
# scan it if info is old or not existent
def lookupFile(malw):

    client = vt.Client("<API-KEY>")
    file = client.get_object(malw.path) 

    # need to check to see if a file already has info
    # also need to check the last scan date(fresh info)

    # if the file is unscanned then scan the file
    # this will wait for the scan to be completed
    # this helps to keep the process automated
    with open("pwd of file", "rb") as f:
        analysis = client.scan_file(f, wait_for_completion=True)

    client.close()

# used to lookup a url
# called by user input in shell
def lookupUrl(url):
    client = vt.Client("<API-KEY>")
    analysis = client.scan_url(url)
    
    client.close()

# used to lookup a domain
def lookupDomain(domain):
    pass
