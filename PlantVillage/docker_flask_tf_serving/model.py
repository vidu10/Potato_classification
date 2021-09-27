import tensorflow as tf
import numpy as np
import json
import requests
from io import BytesIO
from PIL import Image

SIZE=256
MODEL_URI='http://localhost:8501/v1/models/potatoes_model:predict'
CLASSES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE))
    img_batch = np.expand_dims(image, 0)

    data = json.dumps({
        'instances': img_batch.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    result = json.loads(response.text)
    prediction = np.array(response.json()["predictions"][0])
    class_name = CLASSES[np.argmax(prediction)]
    return class_name




