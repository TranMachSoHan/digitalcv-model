import pickle
from flask import Flask,jsonify,request
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS
import pandas
import os
import datetime  

import moduleRecommendation 

app = Flask(__name__)

# CORS policy 
CORS(app)

# initialize Recommender Model class 
r = moduleRecommendation.RecommenderModel()

@app.route('/',methods = ['GET'])
def index():
    return 'Hello, from Flask! '

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
    scheduler_task()
    app.run(debug=True)