#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:11:47 2020

@author: monalisha
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) 
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   
    text = request.form['state']
    prediction = model.predict(text)

    

    return render_template('index.html', prediction_text='result should be  {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)