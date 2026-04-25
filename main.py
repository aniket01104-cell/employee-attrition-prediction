from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

model = joblib.load("attrition_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.to_dict()

        for key in data:
            try:
                data[key] = float(data[key])
            except:
                pass

        df = pd.DataFrame([data])

       
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0

        df = df[model.feature_names_in_]

        prob = model.predict_proba(df)[0][1]
        prob = float(prob) if prob is not None else 0.0
        percent = round(prob * 100, 2)

        
        if prob >= 0.90:
            risk = "High Risk"
            reasons = [
                "High workload and overtime",
                "Low job satisfaction",
                "Frequent job switches"
            ]
            solutions = [
                "Improve work-life balance",
                "Increase salary incentives",
                "Provide career growth"
            ]

        elif prob >= 0.40:
            risk = "Medium Risk"
            reasons = [
                "Moderate satisfaction",
                "Limited growth opportunities",
                "Average employee engagement"
            ]
            solutions = [
                "Increase engagement initiatives",
                "Provide upskilling opportunities",
                "Monitor employee satisfaction"
            ]

        else:
            risk = "Low Risk"
            reasons = [
                "High job satisfaction",
                "Stable work environment",
                "Good work-life balance"
            ]
            solutions = [
                "Maintain current policies",
                "Recognize employee performance",
                "Continue engagement strategies"
            ]

        return render_template(
            "result.html",
            percent=percent,
            risk=risk,
            reasons=reasons,
            solutions=solutions
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)