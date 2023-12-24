import numpy as np
import pandas as pd
import config
from utilities import AbaloneAgeDetector
from flask import Flask, render_template,request,json,jsonify

app = Flask(__name__)

@app.route("/")
def Home_App():
    return render_template('index.html')


@app.route("/prediction", methods=['POST','GET'])
def Age_Result():
    if request.method == 'POST':
        data = request.form
        Sex = data['Sex']
        Length = float(data['Length'])
        Diameter = float(data['Diameter'])
        Height  = float(data['Height'])
        Whole_weight = float(data['Whole_weight'])
        Shucked_weight = float(data['Shucked_weight'])
        Viscera_weight = float(data['Viscera_weight'])
        Shell_weight = float(data['Shell_weight'])


        class_instance = AbaloneAgeDetector(Sex,Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight)

        output = class_instance.predict_age()

    return render_template('index.html',result = output)

if __name__=="__main__":
    app.run(debug=True, port=config.PORT, host=config.HOST)

