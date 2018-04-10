import requests
import json

CountryCode='US'
API_URL='http://services.groupkt.com/country/get/iso2code/%s' % (CountryCode)

Result = requests.get(API_URL,headers={'content-type': 'application/json'},verify=False)
if Result.status_code==200:
    print (Result.text)
    ResultJSON=json.loads(Result.text)

    print (ResultJSON)
    print (ResultJSON['RestResponse'])
    print (ResultJSON['RestResponse']['result'])
    print (ResultJSON['RestResponse']['result']['alpha3_code'])


