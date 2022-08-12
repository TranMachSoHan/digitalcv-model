from flask import Flask,jsonify,request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import os
import RecommenderModel 


app = Flask(__name__)

# 
CORS(app)

@app.route('/')
def index():
    return 'Hello, from Flask!'

@app.route("/recommend", methods = ['GET'])
def recommend():
    req_data = request.get_json()
    courseList = req_data['courseList']
    print(courseList)
    r = RecommenderModel.rcmd(courseList)
    print(r)
    return jsonify(r)
      

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)