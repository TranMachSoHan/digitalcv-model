import pickle
from flask import Flask,jsonify,request
import RecommenderModel 
import joblib
import pandas

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def index():
    return 'Hello, from Flask!'

@app.route('/load_data', methods = ['GET'])
def load_data():
    try:
        with open('pickle_folder/rules.pkl', 'rb') as f:
            lookup_table = pickle.load(f) 
    except Exception as e:
        return f"Exception {e}"
    return f"my_pickle : {lookup_table}"

@app.route("/recommend", methods = ['GET'])
def recommend():
    # get request param json 
    req_data = request.get_json()
    courseList = req_data['courseList']

    # avoid joblib cannot read pickle file 
    try:
        r = RecommenderModel.rcmd(courseList)
    except Exception as e:
        return f"Exception {e}"

    # return json type 
    return jsonify(r)
      

if __name__ == '__main__':
    app.run(debug=True)