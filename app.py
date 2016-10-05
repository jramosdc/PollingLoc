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
line1= data['pollingLocations'][0]['address']['city']
line2= data['pollingLocations'][0]['address']['line1']
line3= data['pollingLocations'][0]['address']['locationName']
line4= data['pollingLocations'][0]['address']['state']
line5= data['pollingLocations'][0]['pollingHours']
final=u''.join("<p>%s<p> %s<p> %s<p> %s<p> %s<p>" % (line1, line2, line3, line4, line5)).replace('[',' ').replace(']',' ')
print (final)


