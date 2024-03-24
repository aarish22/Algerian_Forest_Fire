import pickle
import pandas as pd
import numpy as np
from flask import Flask,request,jsonify,render_template
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

#import rigde regressor model and standard scaler
ridge_model=pickle.load(open('Models1/ridge.pkl','rb'))
standard_scaler=pickle.load(open('Models1\scaler (1).pkl','rb'))

## route for home page
@app.route('/')
def index():
    return render_template('index.html')


    
@app.route('/predictdata',methods=['GET','POST'])
def predict_score():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        Rh=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        Ffmc=float(request.form.get('FFMC'))
        Dmc=float(request.form.get('DMC'))
        Isi=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
    else:
        return render_template('Home.html')
    
    new_data_scaled=standard_scaler.transform([[Temperature,Rh,Ws,Rain,Ffmc,Dmc,Isi,Classes,Region]])
    Result=ridge_model.predict(new_data_scaled)
    
    return render_template('Home.html',Result=Result[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0")