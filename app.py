from flask import Flask, request, render_template
import pickle, numpy as np

app  = Flask(__name__)

# ---- load model + class names ---------------------------------------------
bundle  = pickle.load(open("model.pkl", "rb"))
model   = bundle["model"]
classes = bundle["classes"]              # ['Gryffindor', 'Hufflepuff', …]

ORDER = ["bravery","ambition","intelligence",
         "loyalty","creativity","dark_arts_knowledge"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = np.array([[float(request.form[f]) for f in ORDER]])
    house_id = model.predict(features)[0]
    house    = classes[house_id]
    return render_template("index.html",
        prediction_text=f"🏰 The Sorting Hat says: <strong>{house}!</strong>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
