import urllib2
import json, requests

# Automatically geolocate the connecting IP
##f = urllib2.urlopen('http://freegeoip.net/json/')
##json_string = f.read()
##f.close()
##location = json.loads(json_string)
##coord= "{},{}".format(location['latitude'],location['longitude'])

url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'

params = dict(
    address='72+Frambes+Ave,+Columbus,+OH+43201',
    electionId='2000',
    fields='pollingLocations',
    key='AIzaSyAzNEkhYYRuLAgVU2ghn1LY9ulanWBd1x0'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print json.dumps(data, indent=4, sort_keys=True)


