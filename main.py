'''
    Author: Jordan Madden
    Description: ECSE3038 Lab 2
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Super fancy database
PROFILE_DB = {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "neddamj_",
            "role": "Student engineer",
            "color": "blue"
        }
    }

TANK_DB = []
max_id = 0

@app.route("/")
def home():
    return "ECSE3038 - Lab 2"

# Returns all of the data in the database
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def get_profile():
    if request.method == "GET":
        return jsonify(PROFILE_DB)

    elif request.method == "POST":
        # Get the current date and time
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")

        PROFILE_DB["data"]["last_updated"] = (dt)
        PROFILE_DB["data"]["username"] = (request.json["username"])
        PROFILE_DB["data"]["role"] = (request.json["role"])
        PROFILE_DB["data"]["color"] = (request.json["color"])

        return jsonify(PROFILE_DB)

    elif request.method == "PATCH":
        # Get the current date and time
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
    
        data = PROFILE_DB["data"]

        r = request.json
        r["last_updated"] = dt
        attributes = r.keys()
        for attribute in attributes:
            data[attribute] = r[attribute]

        return jsonify(PROFILE_DB)    


###############################################################################

# Returns all of the data in TANK_DB
@app.route("/data", methods=["GET", "POST"])
def tank_data():
    if request.method == "GET":
        return jsonify(TANK_DB)  

    elif request.method == "POST":
        global max_id

        max_id += 1

        r = request.json
        r["id"] = max_id
        TANK_DB.append(r)
        return jsonify(TANK_DB)
   
 
@app.route('/data/<int:id>', methods=["PATCH", "DELETE"])
def tank_id_methods(id):
    if request.method == "PATCH":
        for i in TANK_DB:
            if i["id"] == id:
                r = request.json
                attributes = r.keys()

                for attribute in attributes:
                    i[attribute] = r[attribute]

        return jsonify(TANK_DB)
    
    elif request.method == "DELETE":
        for i in TANK_DB:
            if i["id"] == id:
                TANK_DB.remove(i)

        return jsonify(TANK_DB)

if __name__ == "__main__":
    app.run(
        debug=True,
        port = 3000
    )