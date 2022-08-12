from flask import Flask,jsonify,request
import RecommenderModel 


app = Flask(__name__)


@app.route('/',methods = ['GET'])
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
    app.run()