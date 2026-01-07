from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load(open('Models/car_prediction_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        car_model = request.form.get('car_model')
        year = int(request.form.get('year'))
        km_driven = int(request.form.get('km_driven'))
        fuel_type = request.form.get('fuel_type')
        seller_type = request.form.get('seller_type')
        transmission_type = request.form.get('transmission_type')
        
       
        mileage = float(request.form.get('mileage'))
        engine = float(request.form.get('engine'))
        max_power = float(request.form.get('max_power'))
        seats = int(request.form.get('seats'))

       
        vehicle_age = 2025 - year 
        
       
        input_data = pd.DataFrame({
            'Unnamed: 0': [0], 
            'model': [car_model],
            'vehicle_age': [vehicle_age],
            'km_driven': [km_driven],
            'seller_type': [seller_type],
            'fuel_type': [fuel_type],
            'transmission_type': [transmission_type],
            'mileage': [mileage],
            'engine': [engine],
            'max_power': [max_power],
            'seats': [seats],
            'year': [year] 
        })

       
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Estimated Car Price: ₹{output}')

if __name__ == "__main__":
    app.run(debug=True)