# Test modelo
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array


image_size = (200, 200)

# Cargar el modelo
model = tf.keras.models.load_model('tensorflow_nn.h5')

# Cargar una imagen de prueba
img = load_img("./images/0-up/43.png", color_mode='grayscale', target_size=(200,200))
plt.imshow(img)
plt.show()
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

#Realizar la predicción
prediction = model.predict(img_array)
print(f'Predicción: {prediction}')
predicted_class = np.argmax(prediction)
print(f'Predicción: {predicted_class}')
