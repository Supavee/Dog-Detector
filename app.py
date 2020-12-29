from __future__ import division, print_function

# coding=utf-8
import sys
import os
import glob
import re
from pathlib import Path



# Import fast.ai Library
from fastai import *
from fastai.vision import *

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# from sklearn import datasets
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import LinearSVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (brier_score_loss, precision_score, recall_score,
#                              f1_score)
# from sklearn.calibration import CalibratedClassifierCV, calibration_curve
# from sklearn.model_selection import train_test_split

# Define a flask app
app = Flask(__name__)



path = Path("path")
classes = ['Not Found','Dougie', 'Finn', 'Hana', 'KaoJao', 'Kiara', 'Luke', 'Manny', 'Maple', 'Maya', 'Ninja', 'Topi']

# dougie = "Dougie　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　USER NAME : John\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. : 0971530463\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n5/75-6 Soi Samarnmitr New Rd\n Bang Korlaem Bangkholeam 10120,\n Bangkok, Thailand"
# finn = "Finn　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jim\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 TEL. : 023456981\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\nCharoen Krung 32 Rd.Si Phra Ya Bangrak,\nBangkok,10500,Thailand"
# Hana = "Hana　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jam\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. : 0964626636\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\nL House, 110 Soi Lat Phrao 8 Yaek 9, Chom Phon,\nChatuchak, Bangkok 10900, Thailand"
# KaoJao = "KaoJao　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jay\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0863459871\　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n  2/30 Moo.1 Soi.Rama 2(25) T.Bangmod\nA.chom Thong, Bangkok, 10150, Thailand"
# Kiara ="Kiara　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jew\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 025898418\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n153 4Th Floor The Peninsula Plaza Bluilding Ratchadamri Road Lumpini,\nA.chom Thong, Bangkok, 10330, Thailand"
# Luke ="Luke　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jai\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0642369872\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n1/15 Moo 4 Soi Wong Duan Changwattana Rd.,\nBangkok, 10330, Thailand"
# Manny ="Manny　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jack\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0641235987\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n69/55 SOI BANGKADEE 8 Rama Ii Rd. Bangkadee,\nBangkok, 10150, Thailand"
# Maple ="Maple　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jane\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0896354781\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n22/5 Gp 5 Chimplee Chimplee Taling Chan,\nBangkok, 10170, Thailand"
# Maya ="Maya　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jin\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0975624310\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS : \n63 Ratchadaphisek Soi 18 Ratchadaphisek Road Huai Khwang,\nBangkok, 10310, Thailand"
# Ninja ="Ninja　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jo\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. 0862459732\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\n35/119 Soi Maneeya Village Ramintra Klong Goom Buengkhum,\nBangkok, 10230, Thailand"
# Topi="Topi　　　　　　　　　　\n　　　　　　　　　　\nINFORMATION\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　 USER NAME : Jun\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　TEL. : 0612358941\n　　　　　　　　　　\n　　　　　　　　　　\n　　　　　　　　　　ADDRESS :\nTheparak Rd. Muang Samutprakarn Samutprakarn,\nBangkok, 10270, Thailand"

# classes = ['Not Found',dougie,finn,Hana,KaoJao,Kiara,Luke,Manny,Maple,Maya,Ninja,Topi]
data2 = ImageDataBunch.single_from_classes(path, classes, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
learn = cnn_learner(data2, models.resnet34)
learn.load('stage')




def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """
   
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)

    return pred_class
    

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        return str(preds)
    return None


if __name__ == '__main__':

    # app.run()
    app.run(host="127.0.0.1",port=8080,debug=True)


