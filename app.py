import os
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf

app = Flask(__name__)
CORS(app)

def preprocess_image(image):
    image = np.array(image, dtype=np.float32) / 255
    image = np.expand_dims(image, axis=-1)  # Add the channel dimension
    image = np.expand_dims(image, axis=0)  # Add the batch dimension
    return image

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    image = Image.open(image_file).convert('L').resize((28, 28))
    image_array = np.array(image)
    preprocessed_image = preprocess_image(image_array)
    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction[0])
    return jsonify({'prediction': str(predicted_class)})

if __name__ == '__main__':
    model = tf.keras.models.load_model('mnist_model', compile=False)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
