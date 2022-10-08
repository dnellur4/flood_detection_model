from pathlib import Path  # if you haven't already done so

file = Path(_file_).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

from cgitb import text
from imp import load_module
from pickle import GET
import flask
from requests import request
from sklearn.svm import SVC
from sentence_transformers import SentenceTransformer
import pickle
import os
import argparse
from src.Application.modelprediction import ModelPrediction

flask_app = flask.Flask(__name__)
def run_app():
    flask_app.run(port =3000, debug =True)
        
def return_app():
        return(flask_app)

@flask_app.route("/",methods = ['POST','GET'])
def Home():
    try:
        username = flask.request.form.get('user')
        return flask.render_template("index.html", usrname = username)
    except:
        return flask.render_template("index.html")

@flask_app.route("/predict", methods = ['POST','GET'])
def predict():
            #loading the tokenizer
            res = ''
            description=''
            mp = ModelPrediction()
            if flask.request.method == 'POST':
                ptext= flask.request.form.get('post_text')
                print(ptext)
                description= flask.request.form.get('desc')
                loaded_model,svm_model = mp.get_model()
                input_txt = loaded_model.encode(ptext)
                input_title = loaded_model.encode(description)
                input_list = input_txt.tolist() + input_title.tolist()
                result = mp.get_predictions(input_list)
                if result[0] == 1:
                    res = 'The post queried signifies flood'
                else:
                    res= 'The post queried does not signify a flood'
                # return ptext+description
            try:
                username = flask.request.form.get('user')
                return flask.render_template('predict.html',prediction_text = "prediction: {}".format(res),entered_text = description, usrname = "Welcome " + username)
            except:
                return flask.render_template('predict.html',prediction_text = "prediction: {}".format(res),entered_text = description)

@flask_app.route("/login_socialmedia", methods = ['POST','GET'])
def login_socialmedia():
            return flask.render_template("login_socialmedia.html")

if __name__ == '__main__':
    run_app()
