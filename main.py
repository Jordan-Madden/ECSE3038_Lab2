'''
    ECSE3038 Tutorial 1
    Description: Build a basic HTTP REST API with Flask
'''

from flask import Flask, request, jsonify
from copy import deepcopy
import json

app = Flask(__name__)

# Super fancy database
SUPER_DB = [
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

# Returns all of the data in the database
@app.route("/profile", methods=["GET"])
def get_profile():
    return jsonify(SUPER_DB)

# Returns whatever object it recieves in the body of the request
@app.route("/profile", methods=["POST"])
def post_profile():
    copy_db = deepcopy(SUPER_DB)
    c = copy_db[0]
    c["data"] = request.json
    SUPER_DB.append(c)
    return request.json


# Returns 
@app.route('/profile', methods=["PATCH"])
def patch_profile(id):
    for i in SUPER_DB:
        if i["id"] == id:
            i["name"] = request.json
    return request.json

###############################################################################

# Returns all of the data in SUPER_DB
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(SUPER_DB)

# Returns whatever object it recieves in the body of the request
@app.route("/data", methods=["POST"])
def post_data():
    SUPER_DB.append(request.json)
    return request.json

# Returns 
@app.route('/data/<int:id>', methods=["PATCH"])
def patch_data(id):
    for i in SUPER_DB:
        if i["data"] == id:
            i["name"] = request.json
    return request.json

# Returns 
@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    for i in SUPER_DB:
        if i["id"] == id:
            SUPER_DB.remove(i)
    return request.json


if __name__ == "__main__":
    app.run(
        debug=True
    )