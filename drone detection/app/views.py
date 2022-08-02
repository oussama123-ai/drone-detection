from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import gnb_model
from app.utils import Linear_Svc_model
from app.utils import Kneighbors_model

import csv
import cv2
UPLOAD_FLODER = 'static/uploads'
SAVE_FOLDER = 'static/files'

def index():
    return render_template('index.html')

   

def result():
 
    if request.method == "POST":
        f = request.files['fichier']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        # prediction (pass to pipeline model)
        Y=gnb_model(path,filename)
        return render_template('result.html',fileupload=True,inf=Y)

    return render_template('result.html',fileupload=False,img_name="freeai.png")
def result1():
 
    if request.method == "POST":
        f = request.files['fichier']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)

        # prediction (pass to pipeline model)
        Y=Kneighbors_model(path,filename)
        return render_template('result1.html',fileupload=True,inf=Y)

    return render_template('result1.html',fileupload=False,img_name="freeai.png")
def result2():
 
    if request.method == "POST":
        f = request.files['fichier']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
    
        # prediction (pass to pipeline model)
        Y=Linear_Svc_model(path,filename)
        return render_template('result2.html',fileupload=True,inf=Y)

    return render_template('result2.html',fileupload=False,img_name="freeai.png")   

