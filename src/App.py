from cgitb import text
from pickle import GET
#from flask import Flask, request, jsonify, render_template
import flask
from requests import request
from sklearn.svm import SVC
from sentence_transformers import SentenceTransformer
import pickle
import os
import argparse

#filename = '/Users/VKANAMA/Downloads/deep_model.sav'
filename = 'deep_model.sav'
if not os.path.exists(filename):
    print(1)
    os.system("gdown 1Vd1TV-MFHqC4IWbJCGcmKreCf5Jx_au_")
loaded_model = pickle.load(open(filename, 'rb'))

#loading the model
#filename = '/Users/VKANAMA/Downloads/svm_model.sav'
filename = 'svm_model.sav'
if not os.path.exists(filename):
    os.system("gdown  1lg3_Ni8r5p1CK9W3DAPsJuM1lyNt8U4a")
svm_model = pickle.load(open(filename, 'rb'))

flask_app = flask.Flask(__name__)

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
    if flask.request.method == 'POST':
        ptext= flask.request.form.get('post_text')
        print(ptext)
        description= flask.request.form.get('desc')
        input_txt = loaded_model.encode(ptext)
        input_title = loaded_model.encode(description)
        input_list = input_txt.tolist() + input_title.tolist()
        result = svm_model.predict([input_list])

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

def return_app():
    return(flask_app)

if __name__ == '__main__':
    flask_app.run(port =3000, debug =True)
