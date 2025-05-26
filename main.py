import streamlit as st
import numpy as np
import pickle


def main():
    # Suppress warnings
    import warnings
    warnings.filterwarnings("ignore")

    # Load the trained model
    with open("model.pkl", "rb") as f:
        loaded_model = pickle.load(f)

    # Streamlit UI

    st.title("🏦 Loan Approval Prediction")

    st.write("Please enter the following details to check if your loan will be approved.")

    # Input fields
    applicant_income = st.number_input("Applicant Income", min_value=0.0, value=0.0,step=100.00)
    coapplicant_income = st.number_input("Co-applicant Income", min_value=0.0, value=0.0,step=100.00)
    credit_history = st.selectbox("Credit History", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    dependents = st.selectbox("Dependents", options=["0", "1", "2", "3+"])
    education = st.selectbox("Education", options=["Graduate", "Not Graduate"])
    gender = st.selectbox("Gender", options=["Male", "Female"])
    loan_amount = st.number_input("Loan Amount",min_value=100,value=1000)
    loan_amount_term_years = st.number_input("Loan Amount Term (in years)", min_value=1.0,max_value=15.0, value=1.0,step=1.0)
    loan_amount_term = loan_amount_term_years * 12  # Convert to months
    married = st.selectbox("Marital Status", options=["Yes", "No"])
    property_area = st.selectbox("Property Area", options=["Urban", "Semiurban", "Rural"])
    self_employed = st.selectbox("Self Employed", options=["No", "Yes"])

    if st.button("Predict Loan Approval"):
        # Encode categorical inputs
        Gender = 1 if gender.lower() == "male" else 0
        Married = 1 if married.lower() == "yes" else 0
        Dependents = min(int(dependents.replace("+", "")), 3)
        Education = 0 if education.lower() == "graduate" else 1
        Self_Employed = 1 if self_employed.lower() == "yes" else 0
        Credit_History = int(credit_history)
        Property_Area = {"rural": 0, "semiurban": 1, "urban": 2}.get(property_area.lower(), 2)

        # Feature engineering
        LoanAmount = np.log(loan_amount + 1)
        Loan_Amount_Term = np.log(loan_amount_term + 1)
        TotalIncome = np.log(applicant_income + coapplicant_income + 1)

        # Final feature vector
        predictionData = [Gender, Married, Dependents, Education, Self_Employed,
                        LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, TotalIncome]

        # Make prediction
        result = loaded_model.predict([predictionData])

        # Output result
        result_text = "✅ Loan will be approved" if result[0] == 1 else "❌ Loan will NOT be approved"
        if result_text=="✅ Loan will be approved":
            st.balloons()
        st.subheader("Prediction Result:")
        st.success(result_text) if result[0] == 1 else st.error(result_text)
        


    ##disclaimer
    st.markdown("---")
    st.markdown("🔔 **Disclaimer:** This is an educational project. The prediction results are for learning purposes only and should not be used for real-world financial or loan decisions.")

if __name__=="__main__":
    main()