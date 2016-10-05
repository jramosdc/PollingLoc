from flask import Flask
from flask import request
from flask import render_template
import urllib2
import json, requests
from googlemaps import GoogleMaps


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("myform.html")

@app.route('/', methods=['POST'])
def my_form_post():

    coord = request.form['coordinates']
    gmaps = GoogleMaps('AIzaSyDOglPws4TcoEFJ8O4gTYl9Pst-KFjsD8E')
    url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    params = dict(address= coord, electionId='2000',fields='dropOffLocations,earlyVoteSites,normalizedInput,pollingLocations',key='AIzaSyAzNEkhYYRuLAgVU2ghn1LY9ulanWBd1x0')
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    line1= data['pollingLocations'][0]['address']['city']
    line2= data['pollingLocations'][0]['address']['line1']
    line3= data['pollingLocations'][0]['address']['locationName']
    line4= data['pollingLocations'][0]['address']['state']
    line5= data['pollingLocations'][0]['pollingHours']
    line5= lat, lng = gmaps.address_to_latlng(coord)
    return render_template('result.html', line1=line1,line2=line2,line3=line3,line4=line4,line5=line5)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
