from distutils.log import debug
from flask import Flask,jsonify,request
import RecommenderModel 
import os 
import pickle

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def index():
    return 'Hello, from Flask!'

@app.route('/load_data', methods = ['GET'])
def load_data():
    pickle_file = os.path.dirname(os.path.abspath(__file__))+'/pickle_folder/rules.pkl'
    with open(pickle_file, 'rb') as handle:
        lookup_table = pickle.load(handle)
    return f"my_pickle : {pickle_file} {lookup_table}"

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