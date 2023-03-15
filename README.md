# MNIST-KERAS-FLASK-JS

This repository contains a simple web application that uses Keras and Flask to create an MNIST digit recognition model. The application allows users to upload an image or draw on an HTML canvas to get digit predictions.

## Features

- Keras-based MNIST digit recognition model
- Flask server for serving the model
- Web interface to test the model with uploaded images or drawings on an HTML canvas

## Requirements

Make sure you have the following Python packages installed:

- Flask==2.1.1
- Flask-CORS==3.0.10
- tensorflow==2.6.0
- Keras==2.6.0
- numpy==1.19.5
- Pillow==9.0.1
- protobuf==3.20.1

You can install the required packages using the following command:

````
pip install -r requirements.txt
````

## Docker

The application can be built and run using Docker. To build the Docker image, run the following command in the project directory:
````
docker build -t mnist-keras-flask-js .
````


To run the Docker container, use the following command:

````
docker run -p 5000:5000 mnist-keras-flask-js
````


The application will be available at `http://127.0.0.1:5000`.

## Usage

There are two web pages available for testing the model:

1. **test-api.html**: This page allows you to upload an image to test the MNIST prediction model. The prediction result will be displayed below the image upload form.
2. **canvas_drawing.html**: This page allows you to draw a digit on an HTML canvas. The MNIST prediction model will predict the digit based on your drawing, and the prediction result will be displayed next to the canvas.

To access these pages, you can either run the Flask server locally or use the Docker container as described above. Then, navigate to `http://127.0.0.1:5000/static/test-api.html` or `http://127.0.0.1:5000/static/canvas_drawing.html` in your web browser.
