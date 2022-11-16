from flask import Flask, render_template, request, redirect, url_for
from utils import *
import sys

app = Flask(__name__)
pred = -1

@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        global pred

        if pred == 1:
            pred_result = "You are eligible for a loan!"
            desc = ""
        elif pred == 0:
            pred_result = "I am sorry, You are not eligible for a loan!"
            desc = ""
        else:
            pred_result = " Belum melakukan prediksi"
            desc = ""
        return render_template("index.html", prediction=pred_result, description=desc)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        
        for key, value in res.items():
            inputs.append(float(value))
        arr_input = [inputs]

        # print(arr_input, file=sys.stdout)
        pred = prediction('./sil_kbs/sil_kbs_env/finalized_model.sav', arr_input)
        # print(pred, file=sys.stdout)
    return redirect(url_for('index'))

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)