# import flask
from flask import Flask, render_template, request, redirect, url_for
import joblib
import pickle

app = Flask(__name__)
loaded_model = joblib.load('./model.pkl')

@app.route("/")

def root():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def make_prediction():

    if request.method == 'POST':
        exp = request.form['exp']
        X = [[float(exp)]]
        [prediction] = loaded_model.predict(X)
        salary = round(prediction, 2)
    msg = "Standard salary for provided experience of  " + str(exp) + " years, would be: $ " + str(salary) + "/-- "

    return render_template("index.html", prediction_text= msg)


if __name__ == '__main__':
    app.run(debug=True)
