from __future__ import print_function
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

# template for a json response from the VT docs
def lookup(file) -> str:
    API_KEY = 'API KEY HERE'

    # send the file hash as the identifier
    virusEncoded = file.encode('utf-8')
    VIRUS_MD5 = hashlib.md5(virusEncoded).hexdigest

    vt = VirusTotalPublicApi(API_KEY)

    response = vt.get_file_report(VIRUS_MD5)

    # return to main for processing
    report = json.dumps(response, sort_keys=False, indent=4)
    
    print(report)

    return report
