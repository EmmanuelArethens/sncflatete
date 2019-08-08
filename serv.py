from flask import Flask
from SNCF import *

app = Flask(__name__)
sncf = sncf()

@app.route('/')
def get_data():
    sncf.requetes()
    l = sncf.get_next_departures()
    chn = "".join(l)
    return chn

@app.route('/1')
def get_datas():
    sncf.requetes()
    l = sncf.get_next_departures()
    r = l[1]
    chn = "".join(r)
    return chn

#if __name__ == "__main__":
# app.run(debug=True)