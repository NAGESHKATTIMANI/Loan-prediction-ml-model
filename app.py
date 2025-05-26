from flask import Flask, render_template, request
import numpy as np
import pickle
import math

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            # Get form inputs
            gender = request.form.get("gender")
            married = request.form.get("married")
            dependents = request.form.get("dependents")
            education = request.form.get("education")
            self_employed = request.form.get("self_employed")
            applicant_income = float(request.form.get("applicant_income"))
            coapplicant_income = float(request.form.get("coapplicant_income"))
            loan_amount = float(request.form.get("loan_amount"))
            loan_term_years = float(request.form.get("loan_term"))
            credit_history = int(request.form.get("credit_history"))
            property_area = request.form.get("property_area")

            # Encode
            Gender = 1 if gender == "Male" else 0
            Married = 1 if married == "Yes" else 0
            Dependents = min(int(dependents.replace("+", "")), 3)
            Education = 0 if education == "Graduate" else 1
            Self_Employed = 1 if self_employed == "Yes" else 0
            Property_Area = {"Rural": 0, "Semiurban": 1, "Urban": 2}.get(property_area, 2)

            # Features
            LoanAmount = np.log(loan_amount + 1)
            Loan_Amount_Term = np.log((loan_term_years * 12) + 1)
            TotalIncome = np.log(applicant_income + coapplicant_income + 1)

            features = [Gender, Married, Dependents, Education, Self_Employed,
                        LoanAmount, Loan_Amount_Term, credit_history, Property_Area, TotalIncome]

            prediction = model.predict([features])
            result = "✅ Loan will be approved" if prediction[0] == 1 else "❌ Loan will NOT be approved"
        except:
            result = "⚠️ Invalid input. Please check your values."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
