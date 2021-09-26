# Potato_classification
At powershell
1. docker run -it -v "C:\Users\Vedansh Agarwal\Downloads\PlantVillage\saved_models:/plantvillage" -p 8501:8501 --entrypoint /bin/bash tensorflow/serving

2. tensorflow_model_server   --rest_api_port=8501   --model_name=potato_disease   --model_base_path=/plantvillage/

Flask-
At Anaconda Prompt-
1. navigate to docker_flask_tf_serving
2. conda activate tf
3. python app.py 

React file -
At windows powershell
1. navigate to frontend
2. npm start
