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
    if request.method == 'POST':
        if 'photo' in request.files: 
            try:
                #file = request.files['photo'].seek(0)
                #file = Image.open(request.files['photo'].stream)
                file = request.files['photo']
                print(type(file))
                result = classifyImage(file)
                print('Model classification: ' + result) 
                return "post"
            except Exception as e:
                print(e)
                return "get from Exception"
    else:
        return "get from else"
       
@app.route('/<path:path>')
def index(path=''):
    if MODE == 'development':
        return proxyRequest(DEV_SERVER_URL, path)
    else:
        return render_template("index.html")      

if __name__=='__main__':
    app.run(debug=True)


