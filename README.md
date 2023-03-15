# MNIST-KERAS-FLASK-JS
CNN MNIST model trained on Keras and served on Flask API to simple JS front-end.    

# Docker

Use this command to create the project.  
````
$ docker-compose up --build
````

It will appear on `localhost:5000`, use `test-api.html` to test.  

# Notebooks

## `MNIST_comparison_between_frameworks.ipynb`

Compare ML frameworks to solve MNIST. We check ease of code reading, and training speed on CPU.    
Keras is the best framework (most readable and accurate model), as it also gives feedback on remaining training time.    

## `flask_experiment_with_MNIST_model.ipynb`

Notebook to test a simple inference route on Flask API.   
The JS form needed to call the API is provided at the end of the notebook.    

# Model

`mnist_model` is trained on Keras for 12 iterations and achieves a 99% accuracy score.  
