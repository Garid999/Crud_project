from flask import Flask, request, jsonify #flask backend iin web app iig create hiine , request ni datag huleen avj frontend buyu (React) ruu damjuulna, jsonify ni python gaas JSON ruu horvuulj React uuniig oilgoh bolmjtoi bolgodog
from flask_cors import CORS # (cross origin resource sharing) React app iig port 3000 deer bolon Flask tai haryltn holbootoi bhd tuslana. Ene bhgu bol browser deer ajilahgui shaltgaan ni securitytei holbotoi
from db import get_connection #db.py deer bichsn code ni mysql tei holbogdoh holboos gedgyg zaaj ugnu
app = Flask(__name__) # Flask app create hiine mun haana baigaag ni zaana
CORS(app) # cors iig app iin buh hesegt ajilj bolhor bolgsn frontend bolon backend horondo haryltsah bolomjtoi boln
@app.route("/users", methods=["GET"]) # API endpoint ni users GET ni ugugdlyg unshyh huseltyg avhiig zaana jishe ni http://localhost:5000/users ingj garj irne
def get_users(): # users endpoint duudagdah uyd ajilah funktsudyg door ni bichne 
    conn = get_connection() #mysql tei holbogdn
    cursor = conn.cursor(dictionary=True) # cursor iig uusgen attribute iig nertei ni hamt harulah
    cursor.execute("select * from users") # husnegtiin buh muriig avna 
    rows = cursor.fetchall() # query iig bugdiin rows huvisagchid hadaglana fetchall bugdiin idevhjulne 
    cursor.close() # cursor iig urgelj haaj bh heregtei cursor bur sanah oi ashygladag haahgui bol app udashyrna
    conn.close() #mysql holboltoo haana database ni holboltiin hyzgartai tul haahgui bol shine hereglegch orj irhed aldaa garna
    return jsonify(rows)  # uurchlultgui geer datag mysql deer bga shyg orulj irne


@app.route("/add_user", methods=["POST"]) # adduser endpoint dudagdah uyd post huselt huleen avna ene ni shine ugugdliig avah zoriulalttai
def add_user(): #add user dudagdah uyin functionudyg door ni bichne 
    data = request.json # frontend ees ireh JSon ugugdliig avna (Frontend bol shuuden ilgeegch JSON bol dotorh zahydal, request.JSon bol zahydaliig neged dotorhiig unshyhtai adyl
    conn = get_connection() # database tei holobogdloo
    cursor = conn.cursor() # cursor uuseglee
    cursor.execute(
        "insert into users (name, email) values (%s, %s)",(data["name"], data["email"])
    ) # shine user oruulah sql command mun %s ene ni security tei holbotoi hervee yg mysql deer bichdg command helberer bichvl gadnas ugugdul usgaj nuuts medelel harh tsashlad database iig evdeh bolmjtoi hryn %s ene ni gadnas bichyh ymr ch input iig command gj hulej avhgui zuvhn text gj hulej avna
    conn.commit() # insert delete update geh met ugugdliin uurchlultiig databsed hadaglana
    cursor.close() # cursor oo haala
    conn.close() # database deh holboltiig hala
    return jsonify({"message": "User added"}) # ugugdul nemegdsnii dara garah output message 

@app.route("/delete_user/<int:id>", methods=["DELETE"]) # delete huseltyg avna ghde delete url der zuvhun integer buyu id gar ni delete hiine 
def delete_user(id): # idgar delete hiih uyd ajylag functionuud door bichigdene 
    conn = get_connection() # database tei holbogdlo
    cursor = conn.cursor() # cursor neelee
    cursor.execute("delete from users where id=%s", (id,)) #URL aas irsen utgatai adylhan utgatai muriig users husnegtes vch ustgana
    conn.commit() # insert delete update geh met ugugdliin uurchlultiig databsed hadaglana
    cursor.close() # cursor halaa
    conn.close() # database deerh connection oo haalaa
    return jsonify({"message": "User deleted"}) # ustgagdsnii daraa garch ireh message

if __name__ == "__main__": # main file iig shuud ajiluulj bga uyd l ene code iig ajyluulna
    app.run(debug=True) # flask server asval debug mode bas asna aldaa garval harulj mun code uurchlugduh uyd server auto restart higdene 