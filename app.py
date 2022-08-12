from distutils.log import debug
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
        lookup_table = joblib.load('pickle_folder/rules.pkl')
    except Exception as e:
        return f"Exception {e}"
    return f"my_pickle : {lookup_table}"

@app.route("/recommend", methods = ['GET'])
def recommend():
    req_data = request.get_json()
    courseList = req_data['courseList']
    print(courseList)
    r = RecommenderModel.rcmd(courseList)
    print(r)
    return jsonify(r)
      

if __name__ == '__main__':
    app.run(debug=True)