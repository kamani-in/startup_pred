from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])

        if prediction[0] == 1:
            result = "Startup is Likely to Succeed 🚀"
        else:
            result = "Startup is Likely to Fail ⚠"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="Error in Input")

if __name__ == "__main__":
    app.run(debug=True, port=5008)
