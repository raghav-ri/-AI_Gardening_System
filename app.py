from flask import Flask, jsonify
from predict_crop import get_weather, model, np  # Import prediction logic

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    temperature, humidity = get_weather()
    
    if temperature is not None and humidity is not None:
        # Dummy Rainfall Value
        rainfall = 200  

        # Make prediction
        input_data = np.array([[temperature, humidity, rainfall]], dtype=float)
        predicted_crop = model.predict(input_data)[0]

        return jsonify({
            "temperature": temperature,
            "humidity": humidity,
            "recommended_crop": predicted_crop
        })
    else:
        return jsonify({"error": "Could not fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
