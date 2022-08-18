import pickle
from flask import Flask,jsonify,request
from flask_cors import CORS
import pandas
import os

import moduleRecommendation 

app = Flask(__name__)

# CORS policy 
CORS(app)

# initialize Recommender Model class 
r = moduleRecommendation.RecommenderModel()

@app.route('/',methods = ['GET'])
def index():
    return 'Hello, from Flask!'

@app.route("/recommend", methods = ['POST'])
def recommend():
    # get request param json 
    req_data = request.get_json()
    courseList = req_data['courseList']

    # avoid joblib cannot read pickle file 
    try:
        courseRecommender = r.rcmd(courseList)
    except Exception as e:
        return f"Exception {e}"


    # return json type 
    return jsonify(courseRecommender)
      

if __name__ == '__main__':
    app.run(debug=True)