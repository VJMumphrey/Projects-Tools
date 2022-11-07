from __future__ import print_function
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

# template for a json response from VT from the docs
def VTlookup():
    API_KEY = 'API KEY HERE'

    # test file used to test software like this
    EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
    EICAR_MD5 = hashlib.md5(EICAR).hexdigest

    vt = VirusTotalPublicApi(API_KEY)

    response = vt.get_file_report(EICAR_MD5)
    print(json.dumps(response, sort_keys=False, indent=4))