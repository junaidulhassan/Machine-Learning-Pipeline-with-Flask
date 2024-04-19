from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('churn_analysis.html')


@app.route('/form', methods=['POST','GET'])
def predict():
    with open('/home/junaidulhassan/LangchainProjects/Jupyter_notebook/production_pipeline.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    if request.method == 'POST':
        # Retrieve form data
        surname = request.form['surname']
        credit_score = request.form['creditScore']
        geography = request.form['geography']
        gender = request.form['gender']
        age = request.form['age']
        tenure = request.form['tenure']
        balance = request.form['balance']
        num_of_products = request.form['numOfProducts']
        has_cr_card = int(request.form['hasCrCard'])
        is_active_member = int(request.form['isActiveMember'])
        estimated_salary = request.form['estimatedSalary']

        # Perform prediction here
        arr = np.array([credit_score,geography,gender,age,tenure,balance,
                        num_of_products,has_cr_card,is_active_member,estimated_salary])
        
        arr = arr.reshape(1,-1)
        pred = loaded_model.predict_proba(arr)
        prediction = pred[0][1]
        prediction = (prediction*100)
        prediction = np.round(prediction,2)

        return render_template('churn_analysis.html', prediction=prediction)
    else:
        return render_template('churn_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)
