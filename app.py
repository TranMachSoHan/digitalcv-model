import pickle
from flask import Flask,jsonify,request
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS, cross_origin
import pandas
import os
import datetime  

import moduleRecommendation 

app = Flask(__name__)

# CORS policy 
cors = CORS(app, resources={r"/recommend": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

# initialize Recommender Model class 
r = moduleRecommendation.RecommenderModel()

@app.route('/',methods = ['GET'])
@cross_origin(origin='*',headers=['Content-Type','Access-Control-Allow-Origin'])
def index():
    return 'Hello, from Flask! '

@app.route("/recommend", methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Access-Control-Allow-Origin'])
def recommend():
    # get request param json 
    req_data = request.get_json()
    courseList = req_data['courseList']

    # avoid joblib cannot read pickle file 
    courseRecommender = r.recommend(courseList)
    # try:
        
    # except Exception as e:
    #     return f"Exception {e}"
    # return json type 
    return jsonify(courseRecommender)

   
def test_job():
    print('I am writing...')
    with open("scr.txt", mode='a') as file:
        file.write('Printed string %s recorded at %s.\n' % 
            ("scr", datetime.datetime.now()))
    print("writing done")

def scheduler_task():
    scheduler = BackgroundScheduler()
    # job = scheduler.add_job(test_job, 'cron', day_of_week ='mon-sun', hour=14, minute=5)
    scheduler.add_job(func=test_job, trigger="interval", seconds=20)

if __name__ == '__main__':
    app.run()
