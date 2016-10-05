import urllib2
import json, requests

# Automatically geolocate the connecting IP
f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
coord= "{},{},{}".format(location['city'],location['region_code'],location['zip_code'])

url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'

params = dict(
    address= '1112+West+Ave,+Richmond,+VA+23220',
    electionId='2000',
    fields='dropOffLocations,earlyVoteSites,normalizedInput,pollingLocations',
    key='AIzaSyAzNEkhYYRuLAgVU2ghn1LY9ulanWBd1x0'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print data['pollingLocations'][0]['pollingHours']


