from flask import Flask, redirect, url_for, request
import json
import os
from flask import jsonify
from predict import predictor_function


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def alive():
    return 'alive'

@app.route('/predict', methods = ['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        if predictor_function(dict(request.form)):
            price = predictor_function(dict(request.form))
            price=jsonify(price)
            response = '200 OK'
            return(response + '\n' + price)
        else:
            response = '400 BAD REQUEST'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
