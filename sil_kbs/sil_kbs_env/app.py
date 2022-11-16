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
            pred_result = "You Got a Malignant"
            desc = "Malignant neoplasms are cancerous tumors. They develop when cells grow and divide more than they should. Malignant neoplasms can spread to nearby tissues and to distant parts of your body. Treatment options may include surgery, chemotherapy or radiation therapy. Early detection is key, so be sure to attend all recommended cancer screenings."
            info = "for more info, visit : https://my.clevelandclinic.org/health/diseases/22319-malignant-neoplasm"
        elif pred == 0:
            pred_result = "You Got a Benign"
            desc="A benign tumor is an abnormal but noncancerous collection of cells. It can form anywhere on or in your body when cells multiply more than they should or don’t die when they should. A benign tumor is not malignant. It grows more slowly, has even borders and doesn’t spread to other parts of your body. Many benign tumors don’t require treatment."
            info = "for more info, visit : https://my.clevelandclinic.org/health/diseases/22121-benign-tumor"
        else:
            pred_result = " Belum melakukan prediksi"
            desc = ""
            info = ""
        return render_template("index.html", prediction=pred_result, description=desc, more_info = info)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        
        for key, value in res.items():
            inputs.append(float(value))
        arr_input = [inputs]

        # print(arr_input, file=sys.stdout)
        pred = prediction('./predictflask/envpredict/finalized_model.sav', arr_input)
        # print(pred, file=sys.stdout)
    return redirect(url_for('index'))

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)