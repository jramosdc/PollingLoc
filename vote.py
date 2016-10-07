from flask import Flask
from flask import request
from flask import render_template
import urllib2
import json, requests
import googlemaps


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("myform.html")

@app.route('/', methods=['POST'])
def my_form_post():

    coord = request.form['coordinates']
    # gkeys
    gmaps = googlemaps.Client(key='AIzaSyBeGwaOHTzvL0S6JR3uLqHqTrf0-lzCYwo')
    gdirect=googlemaps.Client(key='AIzaSyB0mTgf48aoIjhLaKVVLqJY_rT0n72nzDE')
    #get voting info from civic info as data var
    url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    params = dict(address= coord, electionId='2000',fields='dropOffLocations,earlyVoteSites,normalizedInput,pollingLocations',key='AIzaSyAzNEkhYYRuLAgVU2ghn1LY9ulanWBd1x0')
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    # Geocoding in lat and lng the person's address
    geocode_result = gmaps.geocode(coord)
    location = geocode_result[0]['geometry']['location']
    latitude, longitude = location['lat'], location['lng']
    # Geocoding name and address of polling location
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
    directions = gdirect.directions(coord, polloc)
    walk = directions[0]['legs']
    distance= walk[0]['distance']['text']
    return render_template('result.html', line1=line1,line2=line2,line3=line3,line4=line4,line5=line5,distance=distance,latpol=latpol,longpol=longpol, latitude=latitude,longitude=longitude)

@app.errorhandler(500)
def internal_error(error):

    return "The address was not correctly written (1100 Main St, Springfield, VA, ZIPCODE). Or your state has not provided official information yet to the API"
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
