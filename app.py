from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)
df = pd.read_csv("cleaned.csv")
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'LinearRegressionModel.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/', methods=['GET','POST'])
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique(), reverse=True)
    fuel_type = sorted(df['fuel_type'].unique())
    

    prediction = ""
    if request.method == "POST":
        ## Get Data From The Input Form
        company = request.form.get('company')
        car_model =request.form.get('car_models')
        year_of_purchase = int(request.form.get('year'))
        fuel = request.form.get('fuel_type')
        kms = int(request.form.get("kilo_driven"))

        input_data = pd.DataFrame([[car_model, company, year_of_purchase, kms, fuel]],
                                  columns=['name','company','year','kms_driven','fuel_type'])
        
        res = model.predict(input_data)[0]
        prediction = f"Rs {np.round(res, 2)}"

    return render_template('index.html', companies=companies, car_models=car_models, year=year, fuel_type=fuel_type, prediction=prediction)    

if __name__ == "__main__":
    app.run(debug=True)