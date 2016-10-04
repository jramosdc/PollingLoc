from flask import Flask
from flask import request
from flask import render_template
import urllib2
import json, requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("myform.html")

@app.route('/', methods=['POST'])
def my_form_post():

    coord = request.form['coordinates']
    url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    params = dict(address= coord, electionId='2000',fields='dropOffLocations,earlyVoteSites,normalizedInput,pollingLocations',key='AIzaSyAzNEkhYYRuLAgVU2ghn1LY9ulanWBd1x0')
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    data= json.dumps(data, indent=4, sort_keys=True)
    return app.response_class(data, content_type='application/json')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
