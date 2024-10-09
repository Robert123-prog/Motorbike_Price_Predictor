from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Controller class for loading the model and preprocessor
class Controller:
    def __init__(self):
        # Load the trained model and preprocessor (ensure these paths are correct)
        self.regressor = joblib.load(
            r'/model/trained_model.pkl')
        self.preprocessor = joblib.load(
            r'/model/preprocessor.pkl')


def predict_price(self, input_data):
        # Transform input data for the model using the preprocessor
        processed_input_data = self.preprocessor.transform(input_data)
        # Predict the price using the loaded model
        predicted_selling_price = self.regressor.predict(processed_input_data)

        # Return the predicted price
        if len(predicted_selling_price) == 1:
            return predicted_selling_price[0]
        else:
            return predicted_selling_price

# Instantiate the controller to load the model and preprocessor
controller = Controller()

# Home route to confirm the API is running
@app.route('/')
def home():
    return 'Motorbike Price Prediction API is running.'

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the POST request
    data = request.get_json()

    # Define the required fields for prediction
    required_fields = ['name', 'year', 'seller_type', 'owner', 'km_driven', 'ex_showroom_price']

    # Validate that all required fields are present in the incoming request
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Create a DataFrame from the received JSON data (must match the model's expected input)
    input_data = pd.DataFrame({
        'name': [data['name']],
        'year': [data['year']],
        'seller_type': [data['seller_type']],
        'owner': [data['owner']],
        'km_driven': [data['km_driven']],
        'ex_showroom_price': [data['ex_showroom_price']]
    })

    # Use the controller to predict the motorbike price
    predicted_price = controller.predict_price(input_data)

    # Return the predicted price as a JSON response
    return jsonify({'predicted_price': round(predicted_price, 2)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
