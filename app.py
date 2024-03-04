from flask import Flask, request, jsonify, render_template
import os
import numpy as np
import pandas as pd
from carPred.pipeline.prediction import PredictionPipeline

app = Flask(__name__) #init flask

@app.route('/', methods=['GET']) #route to display home page
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET']) #route to display train page
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            make=float(request.form['make'])
            model =float(request.form['model'])
            year =float(request.form['year'])
            mileage =float(request.form['mileage'])
            condition =float(request.form['condition'])
            
            
            
       
         
            data = [make, model, year, mileage, condition]
            data = np.array(data).reshape(1, 5)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


        
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port =8080)

