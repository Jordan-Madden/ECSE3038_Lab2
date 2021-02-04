'''
    Author: Jordan Madden
    Description: ECSE3038 Lab 2
'''

from flask import Flask, request, jsonify
from datetime import datetime
from copy import deepcopy
import json

app = Flask(__name__)

# Super fancy database
PROFILE_DB = [
    {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "neddamj_",
            "role": "Student engineer",
            "color": "blue"
        }
    }
]

TANK_DB = []

# Returns all of the data in the database
@app.route("/profile", methods=["GET"])
def get_profile():
    return jsonify(PROFILE_DB)

# Returns whatever object it recieves in the body of the request
@app.route("/profile", methods=["POST"])
def post_profile():
    # Get the current date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    r = request.json
    r["last_updated"] = dt
    PROFILE_DB[0]["data"] = r

    return request.json


# Returns 
@app.route('/profile', methods=["PATCH"])
def patch_profile():
    # Get the current date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    
    data = PROFILE_DB[0]["data"]

    r = request.json
    r["last_updated"] = dt
    attributes = r.keys()
    for attribute in attributes:
        data[attribute] = r[attribute]

    return request.json


###############################################################################

# Returns all of the data in TANK_DB
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(TANK_DB)

# Returns whatever object it recieves in the body of the request
@app.route("/data", methods=["POST"])
def post_data():
    id = len(TANK_DB) + 1
    
    r = request.json
    r["id"] = id
    TANK_DB.append(r)
    return request.json

# Returns 
@app.route('/data/<int:id>', methods=["PATCH"])
def patch_data(id):
    for i in TANK_DB:
        if i["id"] == id:
            r = request.json
            attributes = r.keys()

            for attribute in attributes:
                i[attribute] = r[attribute]

    return request.json

# Returns 
@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    for i in TANK_DB:
        if i["id"] == id:
            TANK_DB.remove(i)

    return {
        "success": True
        }


if __name__ == "__main__":
    app.run(
        debug=True
    )