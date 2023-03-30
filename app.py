from flask import Flask,jsonify,render_template,request
from reverseProxy import proxyRequest
import os
from classifier import classifyImage


MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://192.168.1.17:19000'
prediction='hello Noura'

app = Flask(__name__)

# Ignore static folder in development mode.
if MODE == "development":
    app = Flask(__name__,)


@app.route('/',methods=['GET','POST'])
def classify():
    try:
        if request.method == 'POST':
            if (request.files['photo']): 
                file = request.files['photo']
                result = classifyImage(file)
                print('Model classification: ' + result)   
                return "test 1"     
      
    except Exception as e:
        pass
        print("Exception---->"+e)
        return "test 2"
       
@app.route('/<path:path>')
def index(path=''):
    if MODE == 'development':
        return proxyRequest(DEV_SERVER_URL, path)
    else:
        return render_template("index.html")      

if __name__=='__main__':
    app.run(debug=True)


