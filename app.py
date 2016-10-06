import urllib2
import json, requests
import googlemaps


# Automatically geolocate the connecting IP
#f = urllib2.urlopen('http://freegeoip.net/json/')
#json_string = f.read()
#f.close()
#location = json.loads(json_string)
#coord= "{},{},{}".format(location['city'],location['region_code'],location['zip_code'])

#the address
address= '1112+West+Ave,+Richmond,+VA+23220'
#Get nearest polling station and other fields
url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
params = dict(
    address= address,
    electionId='2000',
    fields='dropOffLocations,earlyVoteSites,normalizedInput,pollingLocations',
    key='AIzaSyDZzzaLfz8BI88BQ_bliCUdkn6Ao4WzQX4'
)
resp = requests.get(url=url, params=params)
# Geocoding in lat and lng the person's address
gmaps = googlemaps.Client(key='AIzaSyBeGwaOHTzvL0S6JR3uLqHqTrf0-lzCYwo')
gdirect=googlemaps.Client(key='AIzaSyB0mTgf48aoIjhLaKVVLqJY_rT0n72nzDE')
geocode_result = gmaps.geocode(address)
location = geocode_result[0]['geometry']['location']
latitude, longitude = location['lat'], location['lng']
# Geocoding name and address of polling location
data = json.loads(resp.text)
line1= data['pollingLocations'][0]['address']['city']
line2= data['pollingLocations'][0]['address']['line1']
line3= data['pollingLocations'][0]['address']['locationName']
line4= data['pollingLocations'][0]['address']['state']
line5= data['pollingLocations'][0]['pollingHours']
polloc=u''.join("%s, %s, %s, %s" % (line3, line2, line1, line4)).replace('[',' ').replace(']',' ')
# Geocoding in lat and lng the polling location
geocode_result = gmaps.geocode(polloc)
geodump= json.dumps(geocode_result)
json_read= json.loads(geodump)
location = geocode_result[0]['geometry']['location']
latpol, longpol = location['lat'], location['lng']
# Find distance
directions = gdirect.directions(address, polloc)
walk = directions[0]['legs']
distance= walk[0]['distance']['text']

print (distance)

