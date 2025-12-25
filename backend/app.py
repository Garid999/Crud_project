from flask import Flask, request, jsonify #flask backend iin web app iig create hiine , request ni datag huleen avj frontend buyu (React) ruu damjuulna, jsonify ni python gaas JSON ruu horvuulj React uuniig oilgoh bolmjtoi bolgodog
from flask_cors import CORS # (cross origin resource sharing) React app iig port 3000 deer bolon Flask tai haryltn holbootoi bhd tuslana. Ene bhgu bol browser deer ajilahgui shaltgaan ni securitytei holbotoi
from db import get_connection #db.py deer bichsn code ni mysql tei holbogdoh holboos gedgyg zaaj ugnu
app = Flask(__name__) # Flask app create hiine mun haana baigaag ni zaana
CORS(app) # cors iig app iin buh hesegt ajilj bolhor bolgsn frontend bolon backend horondo haryltsah bolomjtoi boln
@app.route("/users", methods=["GET"]) # API endpoint ni users GET ni ugugdlyg unshyh huseltyg avhiig zaana jishe ni http://localhost:5000/users ingj garj irne
def get_users(): # users endpoint duudagdah uyd ajilah funktsudyg door ni bichne 
    