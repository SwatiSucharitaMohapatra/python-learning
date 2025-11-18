import urllib.request, urllib.parse
import json, ssl

#URL which is cached for location in map
baseurl = "http://py4e-data.dr-chuck.net/opengeo?"

#Ignoring SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Creating a Query paramterise url for the user entered address
while True:
    address = input('Enter your address: ')
    if len(address) < 1 : break

    address = address.strip()
    params = dict()
    #Define The q paramter in a dictionary and add the whole address
    params['q'] = address

    url = baseurl + urllib.parse.urlencode(params)

    print('Retreiving:', url)

#Get requested data after URL opened
    requestdata = urllib.request.urlopen(url, context=ctx)
    data = requestdata.read().decode()
    #print('Retreived', len(data), 'characters', data[:20].replace('\n', ' '))

#Json Error handling, if any error

    try :
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('====== Download Error =======')
        print(data)

    if len(js['features']) == 0:
        print('====== Object Not found =======')
        print(data)

    #Retreive plus code

    pluscode = js['features'][0]['properties']['plus_code']

    print('Plus code:', pluscode)